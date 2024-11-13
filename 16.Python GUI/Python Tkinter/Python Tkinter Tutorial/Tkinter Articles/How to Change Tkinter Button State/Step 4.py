if __name__ == "__main__":

	# Instantiating top level
	root = Tk()

	# Setting the title of the window
	root.title("Button State App")

	# Setting the geometry i.e Dimensions
	root.geometry("400x250")

	# Calling our App
	app = App(root)

	# Mainloop which will cause
	# this toplevel to run infinitely
	root.mainloop()
