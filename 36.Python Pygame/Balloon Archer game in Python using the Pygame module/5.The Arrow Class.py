# Arrow class consists of all the functions related to the arrows
class Arrow:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed
		self.hit = 0 # Used to track if the arrow has hit any balloon

		self.arrow = pygame.transform.scale(
			pygame.image.load(arrowPath), (width, height))
		self.arrowRect = self.arrow.get_rect()

		# arrow coordinates
		self.arrowRect.x, self.arrowRect.y = posx, posy

	# Method to render the arrow on the screen
	def display(self):
		screen.blit(self.arrow, self.arrowRect)

	# Method to update the position of the arrow
	def update(self):
		self.arrowRect.x += self.speed

	# Method to update the hit variable
	def updateHit(self):
		self.hit = 1

	def getHit(self):
		return self.hit
