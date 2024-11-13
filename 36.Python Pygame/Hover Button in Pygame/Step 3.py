def _create_image(self, color, outline, text, rect):
	img = pygame.Surface(rect.size)
	if outline:
		img.fill(outline)
		img.fill(color, rect.inflate(-4, -3))
	else:
		img.fill(color)

	# render the text once here instead of every frame
	if text != '':
		text_surf = font.render(text, 1, pygame.Color('black'))
		# again, see how easy it is to center stuff using Rect's
		# attributes like 'center'
		text_rect = text_surf.get_rect(center=rect.center)
		img.blit(text_surf, text_rect)
	return img
