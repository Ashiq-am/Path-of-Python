def start_drag(self):
		# Start dragging the bird
		self.dragging = True
		self.drag_start_pos = self.rect.center

	def end_drag(self):
		# Release the bird and set its velocity based on drag direction
		self.dragging = False
		mouse_pos = pygame.mouse.get_pos()
		direction = math.atan2(self.drag_start_pos[1] - mouse_pos[1],
							self.drag_start_pos[0] - mouse_pos[0])
		speed = 10
		self.velocity = [speed * math.cos(direction),
						speed * math.sin(direction)]
