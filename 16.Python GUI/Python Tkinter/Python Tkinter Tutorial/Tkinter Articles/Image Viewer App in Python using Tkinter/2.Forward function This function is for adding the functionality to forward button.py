def forward(img_no):

	# GLobal variable so that we can have
	# access and change the variable
	# whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# This is for clearing the screen so that
	# our next image can pop up
	label = Label(image=List_images[img_no-1])

	# as the list starts from 0 so we are
	# subtracting one
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward",
						command=lambda: forward(img_no+1))

	# img_no+1 as we want the next image to pop up
	if img_no == 4:
		button_forward = Button(root, text="Forward",
								state=DISABLED)

	# img_no-1 as we want previous image when we click
	# back button
	button_back = Button(root, text="Back",
						command=lambda: back(img_no-1))

	# Placing the button in new grid
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)
