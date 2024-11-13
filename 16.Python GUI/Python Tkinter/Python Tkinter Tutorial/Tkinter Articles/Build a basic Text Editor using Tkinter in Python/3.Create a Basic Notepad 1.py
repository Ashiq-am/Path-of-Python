from tkinter import *

root = Tk()
root.geometry("300x300")
root.minsize(height=560,
			width=560)
root.title("Notepad")


# implementing scrollbar functionality
scrollbar = Scrollbar(root)


# packing the scrollbar function
scrollbar.pack(side=RIGHT,
			fill=Y)

root.mainloop()
