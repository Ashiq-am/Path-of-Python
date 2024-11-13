# Block Class
class Block:
	def __init__(self, posx, posy, width, height, color):
		self.posx, self.posy = posx, posy
		self.width, self.height = width, height
		self.color = color
		self.damage = 100

		# The white blocks have the health of 200.
		# So, the ball must hit it twice to break
		if color == WHITE:
			self.health = 200
		else:
			self.health = 100

		# The rect variable is used to handle the placement
		# and the collisions of the object
		self.blockRect = pygame.Rect(
			self.posx, self.posy, self.width, self.height)
		self.block = pygame.draw.rect(screen,
								self.color, self.blockRect)

	# Used to render the object on the screen if and
	# only if its health is greater than 0
	def display(self):
		if self.health > 0:
			self.brick = pygame.draw.rect(screen,
							self.color, self.blockRect)

	# Used to decrease the health of the block
	def hit(self):
		self.health -= self.damage

	# Used to get the rect of the object
	def getRect(self):
		return self.blockRect

	# Used to get the health of the object
	def getHealth(self):
		return self.health
