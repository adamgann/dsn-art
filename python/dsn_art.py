# Main script. Run parser every few seconds. For each spacecraft
# on the board, check its status and update its leds.
import sys
import time
import logging
import argparse
from datetime import datetime

# Git submodule
from parser import DSNParser

# Specific hardware config
from mapping import Mapping
from led import Leds, Status

logger = logging



def main(window, loop_time, verbose=False):
    # Init some objects
    parser = DSNParser()
    hardware = Mapping()
    leds = Leds()
    
    # Initialize logger.
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    fmt = "[%(levelname)s] (%(name)s) %(message)s"
    logger.basicConfig(format=fmt, level=level)
    logger.info(f"Logger initialized.")

    while True:
        try:
            if time_within_window(window):
                data = parser.fetch_data()
                update_sc_leds(data, hardware, leds)
                logger.info(f"Sleep {loop_time} seconds")
            time.sleep(loop_time)
            
            
        except KeyboardInterrupt:
            print("Caught interrupt")
            leds.all_off()
            sys.exit()

def time_within_window(window):
    """Provide a tuple containing two datetimes that 
    define a time window. Return True if the current 
    time is withnin this window, false otherwise."""
    start_time, end_time = window
    current_time = datetime.now().time()
    within_window = start_time.time() < current_time < end_time.time()
    if within_window:
        logger.info("Time is within window. Running display.")
    else:
        logger.info("Time is outside window. No action.")
    return within_window

def update_sc_leds(data, hardware, leds):

    # Init a dictionary from our spaceacraft list to hold parsed status.
    sc_update = dict.fromkeys(hardware.spacecraft, Status.OFF)
    

    for ant in data.keys():
        # Get targets (can be multiple). Filter out 
        # any targets that aren't on the board
        targets_raw = list(data[ant]["targets"].keys())
        targets_low = [x.lower() for x in targets_raw]
        filt_targets = [x for x in targets_low if x in hardware.spacecraft]
        logger.debug(f"Antenna {ant} has {len(filt_targets)} spacecraft on our list active.")
        
        for spacecraft in filt_targets:
            logger.debug(f"Parsing {spacecraft}")
            status = calc_status(data[ant])
            logger.info(f"Found status of {status} for {spacecraft}")
            sc_update[spacecraft] = status
                
    # Now outside the loop, we set status of each spacecraft
    # on the board. This is required to make sure we shut off a
    # spacecraft after it ends contact with DSN. 
    for name, status in sc_update.items():
        logger.debug(f"{name} -> {status}")
        leds.set_group(hardware[name], status)
        
            
def calc_status(ant_dict):
    """Return the Status for the selected spacecraft."""

    # Get data types for uplink and downlink.
    up_type = extract_type(ant_dict["up_signal"])
    down_type = extract_type(ant_dict["down_signal"])
    logger.debug(f"Up: {up_type}  Down: {down_type}")
    
    # If no data/carrier, return None.
    if up_type == down_type == None:
        return Status.OFF
    
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
        return Status.OFF
        
            
def extract_type(sub_ant):
    # Return None if dict is empty
    if not sub_ant:
        return None 
        
    type_str = sub_ant[0]["type"]
    type_val = None if type_str == "none" else type_str
    return type_val

def parse_time_window(input_str):
    try:
        start_str, end_str = input_str.split('-')
        start_time = datetime.strptime(start_str, "%H:%M")
        end_time = datetime.strptime(end_str, "%H:%M")
        return start_time, end_time
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid time window format.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
    help = "Increase output verbosity")
    parser.add_argument("-l", "--loop-time", type=int, 
    default = 60, help="How often in seconds to run loop.",
    dest="loop_time")
    
    # Allow operation within a time window.
    default_window = parse_time_window("08:00-22:00")
    parser.add_argument("--window", type=parse_time_window,
    default = default_window,
    help = "Time window to display LEDS in 24 hour HH:MM-HH:MM format.")
    args = parser.parse_args()
    print(args.window)
    
    main(args.window, args.loop_time, args.verbose)
