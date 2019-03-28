https://shop.pimoroni.com/products/11x7-led-matrix-breakout

11x7 pixels of single-colour, brightness-controlled, message scrolling
goodness!

|Build Status| |Coverage Status| |PyPi Package| |Python Versions|

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've created an easy installation script that will install all
pre-requisites and get your 11x7 LED Matrix Breakout up and running 
with minimal efforts. To run it, fire up Terminal which you'll find 
in Menu -> Accessories -> Terminal on your Raspberry Pi desktop, as 
illustrated below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

    curl https://get.pimoroni.com/matrix11x7 | bash

If you choose to download examples you'll find them in
``/home/pi/Pimoroni/matrix11x7/``.

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    sudo pip3 install matrix11x7

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    sudo pip2 install matrix11x7

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

    sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

In all cases you will have to enable the i2c bus.

Documentation & Support
-----------------------

-  Get help - http://forums.pimoroni.com/c/support

.. |Build Status| image:: https://travis-ci.com/pimoroni/matrix11x7-python.svg?branch=master
   :target: https://travis-ci.com/pimoroni/matrix11x7-python
.. |Coverage Status| image:: https://coveralls.io/repos/github/pimoroni/matrix11x7-python/badge.svg?branch=master
   :target: https://coveralls.io/github/pimoroni/matrix11x7-python?branch=master
.. |PyPi Package| image:: https://img.shields.io/pypi/v/matrix11x7.svg
   :target: https://pypi.python.org/pypi/matrix11x7
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/matrix11x7.svg
   :target: https://pypi.python.org/pypi/matrix11x7
