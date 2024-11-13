import pygame as py

# Initiate pygame and the modules that comes with pygame
py.init()

# setting frame/window/surface with some dimensions
window = py.display.set_mode((300, 300))

# to set title of pygame window
py.display.set_caption("GFG")

# creating image object
image = py.image.load('/home/amninder/Pictures/Wallpapers/download.png')

# to display size of image
print("size of image is (width,height):", image.get_size())

# loop to run window continuously
while True:
	window.blit(image, (0, 0))

	# loop through the list of Event
	for event in py.event.get():
		# to end the event/loop
		if event.type == py.QUIT:

			# it will deactivate the pygame library
			py.quit()
			quit()

		# to display when screen update
		py.display.flip()
