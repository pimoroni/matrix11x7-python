from matrix11x7 import Matrix11x7

import threading

from argparse import ArgumentParser

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty

from .action import Action
from .stoppablethread import StoppableThread

try:
    import http.client as http_status
except ImportError:
    import httplib as http_status

from flask import Blueprint, render_template, abort, request, jsonify, Flask

matrix11x7_blueprint = Blueprint('matrix11x7', __name__)
api_queue = Queue()
matrix11x7 = Matrix11x7()


class AutoScroll():
    _is_enabled = False
    _interval = 0.1

    def config(self, is_enabled="False", interval=0.1):
        self._interval = interval

        if is_enabled == "True":
            if self._is_enabled is False:
                self._is_enabled = True
                self.run()
        else:
            self._is_enabled = False

    def run(self):
        if self._is_enabled is True:
            # Start a timer
            threading.Timer(self._interval, self.run).start()
            # Scroll the buffer content
            matrix11x7.scroll()
            # Show the buffer
            matrix11x7.show()


@matrix11x7_blueprint.route('/autoscroll', methods=["POST"])
def ascroll():
    response = {"result": "success"}
    status_code = http_status.OK

    data = request.get_json()
    if data is None:
        data = request.form
    try:
        api_queue.put(Action("autoscroll", (data["is_enabled"], float(data["interval"]))))
    except KeyError:
        response = {"result": "KeyError", "error": "keys is_enabled and interval not posted."}
        status_code = http_status.UNPROCESSABLE_ENTITY
    except ValueError:
        response = {"result": "ValueError", "error": "invalid data type(s)."}
        status_code = http_status.UNPROCESSABLE_ENTITY

    return jsonify(response), status_code


@matrix11x7_blueprint.route('/scroll', methods=["POST"])
def scroll():
    response = {"result": "success"}
    status_code = http_status.OK

    data = request.get_json()
    if data is None:
        data = request.form
    try:
        api_queue.put(Action("scroll", (int(data["x"]), int(data["y"]))))
    except KeyError:
        response = {"result": "KeyError", "error": "keys x and y not posted."}
        status_code = http_status.UNPROCESSABLE_ENTITY
    except ValueError:
        response = {"result": "ValueError", "error": "invalid integer."}
        status_code = http_status.UNPROCESSABLE_ENTITY

    return jsonify(response), status_code


@matrix11x7_blueprint.route('/show', methods=["POST"])
def show():
    response = {"result": "success"}
    status_code = http_status.OK

    data = request.get_json()
    if data is None:
        data = request.form
    try:
        api_queue.put(Action("write", data["text"]))
    except KeyError:
        response = {"result": "KeyError", "error": "key 'text' not set"}
        status_code = http_status.UNPROCESSABLE_ENTITY

    return jsonify(response), status_code


@matrix11x7_blueprint.route('/clear', methods=["POST"])
def clear():
    response = {"result": "success"}
    status_code = http_status.OK

    api_queue.put(Action("clear", {}))
    return jsonify(response), status_code


@matrix11x7_blueprint.route('/flip', methods=["POST"])
def flip():
    response = {"result": "success"}
    status_code = http_status.OK

    data = request.get_json()
    if data is None:
        data = request.form
    try:
        api_queue.put(Action("flip", (bool(data["x"]), bool(data["y"]))))
    except TypeError:
        response = {"result": "TypeError", "error": "Could not cast data correctly. Both `x` and `y` must be set to true or false."}
        status_code = http_status.UNPROCESSABLE_ENTITY
    except KeyError:
        response = {"result": "KeyError", "error": "Could not cast data correctly. Both `x` and `y` must be in the posted json data."}
        status_code = http_status.UNPROCESSABLE_ENTITY

    return jsonify(response), status_code


def cleanup():
    # Reset the autoscroll
    autoscroll.config()
    # Clear the buffer before writing new text
    matrix11x7.clear()


def run():
    while True:
        action = api_queue.get(block=True)

        if action.action_type == "write":
            cleanup()
            matrix11x7.write_string(action.data)

        if action.action_type == "clear":
            cleanup()

        if action.action_type == "scroll":
            matrix11x7.scroll(action.data[0], action.data[1])

        if action.action_type == "flip":
            matrix11x7.flip(x=action.data[0], y=action.data[1])

        if action.action_type == "autoscroll":
            autoscroll.config(action.data[0], action.data[1])

        matrix11x7.show()


def start_background_thread():
    api_thread = StoppableThread(target=run)
    api_thread.start()


matrix11x7_blueprint.before_app_first_request(start_background_thread)


# Autoscroll handling
autoscroll = AutoScroll()


def main():
    # Parser handling
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", type=int, help="HTTP port.", default=8080)
    parser.add_argument("-H", "--host", type=str, help="HTTP host.", default="0.0.0.0")
    args = parser.parse_args()

    # TODO Check
    matrix11x7.set_clear_on_exit(False)
    matrix11x7.write_string(str(args.port), x=1, y=1, brightness=0.1)
    matrix11x7.show()

    # Flash usage
    app = Flask(__name__)
    app.register_blueprint(matrix11x7_blueprint, url_prefix="/matrix11x7")
    app.run(port=args.port, host=args.host)


if __name__ == '__main__':
    main()
