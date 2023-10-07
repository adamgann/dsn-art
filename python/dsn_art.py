# Main script. Run parser every few seconds. For each spacecraft
# on the board, check its status and update its leds.
import sys

# Git submodule
from pydsn.parser import *

# Specific hardware config
import hardware

# Imports for Adafruit Neopixels
import board, neopixel

# Misc utilities
import time


class DsnArt:
    def __init__(self):
        # Init the DSN web parser
        self.parser = DSNParser()

        # Get the specific hardware configuration
        self.hw = hardware.Hardware()
        self.sc_list = self.hw.get_spacecraft()

        # Setup NeoPixels
        self.pixels = neopixel.NeoPixel(board.D18, 30)

    def update_sc_status(self):
        data = self.parser.fetch_data()
        for ant in data.keys():
            # Get targets (can be multiple)
            targets = list(data[ant]["targets"].keys())
            for spacecraft in targets:
                print(spacecraft)
                print(spacecraft in self.sc_list)
                if spacecraft in self.sc_list:
                    self.set_trx_status(data[ant], spacecraft)

    def set_trx_status(self, ant_dict, sc):
        # Extract type fields: carrier, data, or none
        up_type = ant_dict["up_signal"][0]["type"]
        down_type = ant_dict["down_signal"][0]["type"]
            
        # Handle both, otherwise preference downlink color
        if up_type == down_type:
            self.hw.set_color(sc, "both",up_type)
        else:
            self.hw.set_color(sc, "up", up_type)
            self.hw.set_color(sc, "down", down_type)
        

    def set_leds(self):
        for sc in self.hw.leds:
            pin_list = self.hw.leds[sc]["pins"]
            color_tuple = self.hw.leds[sc]["color"]
            for pin in pin_list:
                self.pixels[pin] = color_tuple

    def main(self):
        while True:
            try:
                # Grab new status and update LEDs
                self.update_sc_status()
                self.set_leds()
                # Wait a few seconds before updating again
                time.sleep(10)
            except KeyboardInterrupt:
                print("Caught interrupt")
                self.hw.all_off()
                self.set_leds()
                sys.exit()


if __name__ == "__main__":
    top = DsnArt()
    top.main()
