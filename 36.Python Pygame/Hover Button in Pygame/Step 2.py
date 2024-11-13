def __init__(self, color, color_hover, rect, callback, text='', outline=None):
	super().__init__()
	self.text = text
	# a temporary Rect to store the size of the button
	tmp_rect = pygame.Rect(0, 0, *rect.size)

	# create two Surfaces here, one the normal state, and one for the hovering state
	# we create the Surfaces here once, so we can simple blit them and dont have
	# to render the text and outline again every frame
	self.org = self._create_image(color, outline, text, tmp_rect)
	self.hov = self._create_image(color_hover, outline, text, tmp_rect)

	# in Sprites, the image attribute holds the Surface to be displayed...
	self.image = self.org
	# ...and the rect holds the Rect that defines it position
	self.rect = rect
	self.callback = callback
