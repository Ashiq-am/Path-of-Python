# Define the Bird class
class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y, image):
		super().__init__()
		# Initialize properties
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.velocity = [0, 0]
		self.dragging = False
		self.drag_start_pos = (0, 0)
