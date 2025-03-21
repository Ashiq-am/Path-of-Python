import pygame as py
import os

# The width and height of our screen
win = py.display.set_mode((200, 280))
py.display.set_caption("Sprite pygame movement")

# Frames per second
FPS = 30

# The main class for our sprite window
class Sprite_Window(py.sprite.Sprite):
	def __init__(self):
		super(Sprite_Window, self).__init__()

		# Name of the folder in which all the
		# images are stored
		folderPath = "Character_images_left"

		# Storing the folder location in a list
		myList = os.listdir(folderPath)
		self.images = []
		for imPath in myList:

			# Appending all the images in the array
			self.images.append(py.image.load(f'{folderPath}/{imPath}'))

		self.index = 0
		self.image = self.images[self.index]
		self.rect = py.Rect(5, 5, 150, 198)

	def update(self):

		# Increase the value of the index by 1
		# so that we can change the sprite images
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]


py.init()
my_sprite = Sprite_Window()
my_group = py.sprite.Group(my_sprite)
clock = py.time.Clock()

# q is here for a boolean value to cancel
# the running window
q = 1
while q:
	for event in py.event.get():
		if event.type == py.QUIT:
			q = 0
	my_group.update()

	# Background image
	bg = py.image.load('hacker.gif')

	win.blit(bg, (1, 1))
	my_group.draw(win)
	py.display.update()
	clock.tick(13)
