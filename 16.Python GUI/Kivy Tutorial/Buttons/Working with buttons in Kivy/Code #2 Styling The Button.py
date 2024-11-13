from tkinter import Button


def build(self):
		# use a (r, g, b, a) tuple
		btn = Button(text ="Push Me !",
				font_size ="20sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				size =(32, 32),
				size_hint =(.2, .2),
				pos =(300, 250))

		return btn







'''These are just similar to the HTML, CSS effects. By this, we fix the position of a button at the 
center of the window, text size, colour and anything you want.'''
