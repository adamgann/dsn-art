# Defines the hardware layout of the LEDs, Pi, etc. 

class Hardware:
	
	def __init__(self):
		self.assign_colors()
		self.assign_leds()
		print("Hardware Setup Complete.")

	def assign_colors(self):
		self.colors = {}
		self.colors['up_carrier'] = (123,123,123)
		self.colors['up_data'] = (0,0,255)
		self.colors['down_data'] = (0,255,0)
		self.colors['down_carrier'] = (34,35,36)

	def assign_leds(self):
		self.leds = {}
		self.leds['JUNO'] = {}
		self.leds['JUNO']['pins'] = [6,7,8]

		self.leds['NHPC'] = {}
		self.leds['NHPC']['pins'] = [9,10,11]

		self.leds['ORX'] = {}
		self.leds['ORX']['pins'] = [12,13,14]

		for key in self.leds:
			self.leds[key]['color'] = (0,0,0)
		#self.leds["NHPC"] = {'pins',[9,10,11],'color',(0,0,0)}
		#self.leds["M20"] = {'pins',[12,13,14],'color',(0,0,0)}

	def get_spacecraft(self):
		return list(self.leds.keys())

	def set_color(self,sc,direction,carrier):
		print(carrier)
		# If no signal or carrier, take no action 
		if carrier == 'none':
			print("nah")
			return 

		# Otherwise, look up carrier/data color in dictionary 
		key = direction + "_" + carrier
		color_tuple = self.colors[key]

		self.leds[sc]['color'] = color_tuple
		print(self.leds)
