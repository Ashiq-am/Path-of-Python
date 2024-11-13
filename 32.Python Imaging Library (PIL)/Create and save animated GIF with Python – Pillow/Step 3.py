for i in range(0, max_radius, step):
	im = Image.new('RGB', (width, width), color_2)
	draw = ImageDraw.Draw(im)
	draw.ellipse((center - i, center - i,
				center + i, center + i),
				fill=color_1)
	images.append(im)
