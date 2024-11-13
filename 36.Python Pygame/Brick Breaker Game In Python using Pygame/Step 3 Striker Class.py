# Striker class
class Striker:
	def __init__(self, posx, posy, width,
				height, speed, color):
		self.posx, self.posy = posx, posy
		self.width, self.height = width, height
		self.speed = speed
		self.color = color

		# The rect variable is used to handle the
		# placement and the collisions of the object
		self.strikerRect = pygame.Rect(
			self.posx, self.posy, self.width, self.height)
		self.striker = pygame.draw.rect(screen,
										self.color, self.strikerRect)

	# Used to render the object on the screen
	def display(self):
		self.striker = pygame.draw.rect(screen,
										self.color, self.strikerRect)

	# Used to update the state of the object
	def update(self, xFac):
		self.posx += self.speed*xFac

		# Restricting the striker to be in between
		# the left and right edges of the screen
		if self.posx <= 0:
			self.posx = 0
		elif self.posx+self.width >= WIDTH:
			self.posx = WIDTH-self.width

		self.strikerRect = pygame.Rect(
			self.posx, self.posy, self.width, self.height)

	# Returns the rect of the object
	def getRect(self):
		return self.strikerRect
