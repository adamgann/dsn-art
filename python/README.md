Code which executes on the Pi to power LED display. Parser module based on github.com/russss/pydsn

### Prerequisites
Code written and tested on RasPi Zero W. Requires the CircuitPython NeoPixel library running on RasPi. Follow [Adafruit instructions](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview). When calling functions in this library you must run as root.

### Install
Installation with pip gives the `dsn-leds` package

```
cd dsn-art/python
pip install .
```
Add this to `/etc/rc.local` to start a background process on startup

```
dsn-leds &
```

### Test 
The LED test module will cycle through each spacecraft on the board
```
python -m tests.led_test
```

