from nicegui import ui

class Demo:
	def __init__(self):
		self.number = 1

demo = Demo()
# creating slider
ui.slider(min=1, max=5).bind_value(demo, 'number')
# creating number
ui.number().bind_value(demo, 'number')
# creating toggle buttons
ui.toggle({1: 'A', 2: 'B', 3: 'C', 4:'D', 5: 'E'}).bind_value(demo, 'number')

ui.run()
