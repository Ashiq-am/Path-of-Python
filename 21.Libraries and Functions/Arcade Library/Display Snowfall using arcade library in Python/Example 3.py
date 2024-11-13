class snow_fall:
	def __init__(self):
		self.x = 0
		self.y = 0

	def reset_snow(self):

		# Reset flake to random position above screen
		self.y = random.randrange(Height, Height + 100)
		self.x = random.randrange(Width)
