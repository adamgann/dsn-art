"""Test the LED installation by lighting up each spacecraft in turn for 1 second."""

import time

# Custom hardware/led configuration
from dsnleds.mapping import Mapping
from dsnleds.led import Leds, Status

def main():
    """Run main test, 1 second per group."""
    hardware = Mapping()
    leds = Leds()

    for spacecraft in hardware.spacecraft:
        # Light up current group
        print(f"Lighting {spacecraft}")
        leds.set_group(hardware[spacecraft], Status.UP_DATA)
        
        # Sleep one second then shut all off.
        time.sleep(1)
        leds.all_off()

if __name__ == "__main__":
    main()
