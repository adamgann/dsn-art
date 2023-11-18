# dsn-art
Live wall art of spacecraft communicating over NASA's Deep Space Network


### Prerequisites
Code written and tested on RasPi Zero W. Requires the CircuitPython NeoPixel library running on RasPi. Follow [Adafruit instructions](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview]. Functions in this library must be run as root.

### Install
Clone repository and dd to `/etc/rc.local` to start a background process on power up, for example:

```
cd /home/pi/src/dsn-art/python && python -m dsnleds &
```

TODO: make a pip-installable package

### Repo Structure
- `eagle/` contains PCB files for the Pi HAT in Eagle CAD
- `images/` contains spacecraft images used to make cutouts
- `python/` contains the dsnleds package which runs on the Pi
