# Draw tiles
def draw_tyle(self):
	pygame.draw.rect(self.screen,
					self.color,
					pygame.Rect(
		self.start_pos_x, self.start_pos_y,
					self.width, self.depth))
	numb = font.render(str(self.num), True,
					(125, 55, 100))
	screen.blit(numb, (self.start_pos_x + 40,
					self.start_pos_y + 10))
