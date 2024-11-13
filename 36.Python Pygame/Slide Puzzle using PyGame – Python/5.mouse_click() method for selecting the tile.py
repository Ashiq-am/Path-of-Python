# when mouse clicks check if a tile is selected or not
def mouse_click(self, x_m_click, y_m_click):
	if x_m_click > self.start_pos_x and x_m_click < self.start_pos_x + self.width and y_m_click > self.start_pos_y and y_m_click < self.start_pos_y + self.depth:
		self.selected = True
	else:
		self.selected = False
