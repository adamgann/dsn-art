# Main script. Run parser every few seconds. For each spacecraft
# on the board, check its status and update its leds.
import sys
import time

# Git submodule
from parser import DSNParser

# Specific hardware config
from mapping import Mapping
from led import Leds, Status


def main():
    # Init some objects
    parser = DSNParser()
    hardware = Mapping()
    leds = Leds()

    while True:
        try:
            data = parser.fetch_data()
            update_sc_leds(data, hardware, leds)
            time.sleep(10)
            
        except KeyboardInterrupt:
            print("Caught interrupt")
            leds.all_off()
            sys.exit()

def update_sc_leds(data, hardware, leds):
    for ant in data.keys():
        # Get targets (can be multiple)
        targets = list(data[ant]["targets"].keys())
        for spacecraft in targets:
            status = calc_status(data[ant])
            print("Status",status)
            print("Spacecraft",spacecraft)
            if status and spacecraft in hardware.spacecraft:
                leds.set_group(hardware[spacecraft], status)
            
def calc_status(ant_dict):
    """Return the Status for the selected spacecraft."""

    # Get data types for uplink and downlink.
    up_type = extract_type(ant_dict["up_signal"])
    down_type = extract_type(ant_dict["down_signal"])
    
    # If no data/carrier, return None.
    if up_type == down_type == None:
        return None
    
    # If both the same, return BOTH status
    if up_type == down_type:
        if up_type == "data":
            return Status.BOTH_DATA
        else:
            return Status.BOTH_CARRIER
    
    # Parse out up/down carrier/data. This is a bit messy. 
    if up_type == None and down_type == "data":
        return Status.DOWN_DATA
    elif up_type == None and down_type == "carrier":
        return Status.DOWN_CARRIER
    elif up_type == "data":
        return Status.UP_DATA
    elif up_type == "carrier":
        return Status.UP_CARRIER
    else:
        return None
        
            
def extract_type(sub_ant):
    # Return None if dict is empty
    if not sub_ant:
        return None 
        
    print(sub_ant)
    type_str = sub_ant[0]["type"]
    type_val = None if type_str == "none" else type_str
    return type_val
    
"""
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

""" 


if __name__ == "__main__":
    main()
