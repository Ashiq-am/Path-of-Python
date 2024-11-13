# when mouse click released unselect the tile by setting False
def mouse_click_release(self, x_m_click_rel, y_m_click_rel):
	if x_m_click_rel > 0 and y_m_click_rel > 0:
		self.selected = False
