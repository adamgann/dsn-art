# Test the LED installation by lighting up each spacecraft in turn for 1 second. 

# Imports for Adafruit Neopixels 
import board, neopixel

# Custom hardware configuration
import hardware

# Misc utilities
import time

class LedTest:
	
	def __init__(self):
		# Setup NeoPixels 
		self.pixels = neopixel.NeoPixel(board.D18,30)

	def main(self):
		
		# Get hardware configuration
		hw = hardware.Hardware()

		for key in hw.leds:
			print("Lighting: {}".format(key))
			self.light_group(hw.leds[key])
			time.sleep(1)
			self.pixels.fill((0,0,0))


	def light_group(self,sc_dict):
		pins = sc_dict['pins']
		for pin in pins:
			self.pixels[pin] = (0,0,255)

	
		


if __name__ == "__main__":
	lt = LedTest()
	lt.main()