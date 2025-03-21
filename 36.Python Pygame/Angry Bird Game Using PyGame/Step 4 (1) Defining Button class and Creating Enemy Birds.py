# Define the Button class
class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, image, action):
		super().__init__()
		# Initialize properties
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.action = action
