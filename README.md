:[11x7 Matrix](matrix11x7-python-logo.png)
https://shop.pimoroni.com/products/matrix11x7-python

11x7 pixels of single-colour, brightness-controlled, message scrolling goodness!

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your 11x7 Matrix
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/matrix11x7 | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/matrix11x7/`.

### Manual install:

#### Library install for Python 3:

```bash
sudo pip3 install matrix11x7
```

#### Library install for Python 2:

```bash
sudo pip2 install matrix11x7
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Get help - http://forums.pimoroni.com/c/support
