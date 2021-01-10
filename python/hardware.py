# Defines the hardware layout of the LEDs, Pi, etc. 

class Hardware:
	
	def __init__(self):
		self.assign_leds()
		print("Hardware Setup Complete.")

	def assign_leds(self):
		self.leds = {}
		self.leds["juno"] = [6,7,8]
		self.leds["msl"] = [9,10,11]
		self.leds["voyager 1"] = [12,13,14]
