"""Set groups of LEDs to certain colors based on status."""
from enum import Enum
import logging

# Imports for Adafruit Neopixels
import board
import neopixel

# Neopixel strip is cut to 30 LEDs
NUM_LEDS = 30

logger = logging.getLogger(__name__)

class Status(Enum):
    """RGB triplet for each type of spacecraft status."""
    OFF = (0, 0, 0)
    UP_DATA = (0, 235, 145)
    DOWN_DATA = (0, 130, 235)
    BOTH_DATA = (225, 0, 235)
    UP_CARRIER = (0, 0, 235)
    DOWN_CARRIER = (0, 0, 235)
    BOTH_CARRIER = (0, 0, 235)


class Leds:
    """Manipulate LEDs."""
    
    def __init__(self):
        self._pixels = neopixel.NeoPixel(board.D18, 30)

    def all_off(self):
        """Set all 30 LEDs off."""
        self.set_all(Status.OFF)

    def set_all(self, status):
        """Set all LEDs to a given status."""
        self._pixels.fill((status.value))

    def set_group(self, pins, status):
        """Set each pin in the list pins to the
        RGB triplet contained in status."""
        for pin in pins:
            self._pixels[pin] = status.value
            logger.debug(f"LED #{pin} to {status.value}")

