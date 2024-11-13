from logging import root
from tkinter import Label, Button
from turtle import forward


def back(img_no):

	# We willl have global variable to access these
	# variable and change whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# for clearing the image for new image to pop up
	label = Label(image = List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="forward",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
						command=lambda: back(img_no - 1))
	print(img_no)

	# whenever the first image will be there we will
	# have the back button disabled
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)
