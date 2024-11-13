def update(self):
	# Update bird's position based on dragging or velocity
	if self.dragging:
		mouse_pos = pygame.mouse.get_pos()
		self.rect.centerx = mouse_pos[0]
		self.rect.centery = mouse_pos[1]
	else:
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]
