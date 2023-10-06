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

		# Lunar Reconnaissance Orbiter
		self.leds['LRO'] = {}
		self.leds['LRO']['pins'] = [0,1,2]

		# Lucy
		self.leds['LUCY'] = {}
		self.leds['LUCY']['pins'] = [3,4,5]

		# Parker Solar Probe
		self.leds['SPP'] = {}
		self.leds['SPP']['pins'] = [6,7,8]

		# Maven
		self.leds['MVN'] = {}
		self.leds['MVN']['pins'] = [9,10,11]

		# New Horizons
		self.leds['NHPC'] = {}
		self.leds['NHPC']['pins'] = [12,13,14]

		# OSIRIS-REX
		self.leds['ORX'] = {}
		self.leds['ORX']['pins'] = [15,16,17]

		# Mars 2020
		self.leds['M20'] = {}
		self.leds['M20']['pins'] = [18,19,20]

		# Top Row
		# Juno
		self.leds['JNO'] = {}
		self.leds['JNO']['pins'] = [21,22,23]

		# MRO
		self.leds['MRO'] = {}
		self.leds['MRO']['pins'] = [24,25,26]

		# Psyche
		self.leds['PSYC'] = {}
		self.leds['PSYC']['pins'] = [27,28,29]





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
