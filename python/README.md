Code which executes on the Pi to power LED display. Parser module based on github.com/russss/pydsn

### Prerequisites
Code written and tested on RasPi Zero W. Requires the CircuitPython NeoPixel library running on RasPi. Follow [Adafruit instructions](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview). When calling functions in this library you must run as root.

### Install
Installation with pip gives the `dsn-leds` package. We'll need a global install so the script can be run as root. Pip's warning about sudo install can be ignored, running this code is really the only thing this board is doing.

```
cd dsn-art/python
sudo pip install .
```
Add this to `/etc/rc.local` to start a background process on startup

```
dsn-leds &
```

### Test 
The LED test module will cycle through each spacecraft on the board
```
python -m tests.test_leds
```

