# Balloon class consists of all the
# functionalities related to the balloons
class Balloon:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed

		self.balloonImg = pygame.image.load(balloonPath)
		self.balloon = pygame.transform.scale(
			self.balloonImg, (self.width, self.height))
		self.balloonRect = self.balloon.get_rect()

		self.balloonRect.x, self.balloonRect.y = posx, posy

	# Method to render the balloon on the screen
	def display(self):
		screen.blit(self.balloon, self.balloonRect)

	# Method to update the position of the balloon
	def update(self):
		self.balloonRect.y -= self.speed

		# If the balloon crosses the upper edge of the screen,
		# we put it back at the lower edge
		if self.balloonRect.y < 0:
			self.balloonRect.y = HEIGHT+10
