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
