"""Run an internal demo without connecting to DSN Eyes. Randomly light up a selection ofspacecraft and then adjust their status every few seconds."""
import time
import random
import argparse

from dsnleds.mapping import Mapping
from dsnleds.led import Leds, Status

class Demo:
	def __init__(self, loop_time):
		self.loop_time = loop_time

		# Init classes
		self.hardware = Mapping()
		self.leds = Leds()

		# Run demo
		self.main()

	def main(self):
		"""Run main demo."""

		# Start with a few randomly-selected spacecraft
		initial_list = random.sample(self.hardware.spacecraft, 5)
		for sat in initial_list:
			self.light_sc_randomly(sat)

		run_loop = True
		while run_loop:
			try:
				# Randomly grab spacecraft from list and change status
				self.light_sc_randomly(random.choice(self.hardware.spacecraft))
				time.sleep(5)
			except KeyboardInterrupt:
				self.leds.all_off()
				run_loop = False
				print("Shut down demo.")


	def light_sc_randomly(self,spacecraft):
		"""Given a spacecraft, randomly set the status and illuminate corresponding LEDS."""
		# Select the status of the spacecraft from enum of possible statuses
		status = random.choice(list(Status))
		print(f"Setting {spacecraft} to {status}.")

		# Illuminate to correct color
		self.leds.set_group(self.hardware[spacecraft], status)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l","--loop-time",dest="loop_time",default=5,type=int,
	help="How often (seconds) to change spacecraft status.")
	args = parser.parse_args()

	Demo(loop_time=args.loop_time)
