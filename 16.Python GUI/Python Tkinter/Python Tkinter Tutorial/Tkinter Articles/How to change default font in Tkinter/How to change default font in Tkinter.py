# Import tkinter.Tk and widgets
from tkinter import Tk, font
from tkinter.ttk import Button, Label


class App:
	def __init__(self, master: Tk) -> None:
		self.master = master

		# Creating a Font object of "TkDefaultFont"
		self.defaultFont = font.nametofont("TkDefaultFont")

		# Overriding default-font with custom settings
		# i.e changing font-family, size and weight
		self.defaultFont.configure(family="Segoe Script",
								size=19,
								weight=font.BOLD)

		# Label widget
		self.label = Label(self.master, text="I'm Label")
		self.label.pack()

		# Button widget
		self.btn = Button(self.master, text="I'm Button")
		self.btn.pack()


if __name__ == "__main__":
	# Top level widget
	root = Tk()

	# Setting window dimensions
	root.geometry("300x150")

	# Setting app title
	root.title("Changing Default Font")

	print(font.names())

	app = App(root)

	# Mainloop to run application
	# infinitely
	root.mainloop()
