class ObstacleClass(pygame.sprite.Sprite):
	def __init__(self, img_path, location, attribute):
		pygame.sprite.Sprite.__init__(self)
		# Set attributes for the obstacle
		self.img_path = img_path
		self.image = pygame.image.load(self.img_path)
		self.location = location
		self.rect = self.image.get_rect()
		self.rect.center = self.location
		# A string representing the type of obstacle (e.g., "tree", "stone", or "flag")
		self.attribute = attribute
		self.passed = False
	def move(self, num):
		# Move the obstacle upwards by subtracting 'num' from its y-coordinate
		self.rect.centery = self.location[1] - num
