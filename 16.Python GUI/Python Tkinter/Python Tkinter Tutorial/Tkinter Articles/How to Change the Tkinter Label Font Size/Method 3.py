# importing tkinter module and Widgets
from tkinter import Tk
from tkinter.font import BOLD, Font
from tkinter.ttk import Label


# Creating App class which will contain Label Widgets
class App:
	def __init__(self, master) -> None:

		# Instantiating master i.e toplevel Widget
		self.master = master

		# Creating first Label i.e with default font-size
		Label(self.master, text="I have default font-size").pack(pady=20)

		# Creating Font, with a "size of 25" and weight of BOLD
		self.bold25 = Font(self.master, size=25, weight=BOLD)

		# Creating second label
		# This label has a default font-family
		# and font-size of 25
		Label(self.master, text="I have a font-size of 25",
			font=self.bold25).pack()


if __name__ == "__main__":

	# Instantiating top level
	root = Tk()

	# Setting the title of the window
	root.title("Change font-size of Label")

	# Setting the geometry i.e Dimensions
	root.geometry("400x250")

	# Calling our App
	app = App(root)

	# Mainloop which will cause this toplevel
	# to run infinitely
	root.mainloop()
