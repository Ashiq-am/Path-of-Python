# Open New Window
def launch():
	global second
	second = Toplevel()
	second.geometry("100x100")

# Change width
def width_slide(x):
	second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")

# Change height
def height_slide(x):
	second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")

# Change both width and height
def both_slide(x):
	second.geometry(f"{int(both_slider.get())}x{int(both_slider.get())}")
