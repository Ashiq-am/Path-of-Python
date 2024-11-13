from tkinter import filedialog


def openfilename():

	# open file dialog box to select image
	# The dialogue box has a title "Open"
	filename = filedialog.askopenfilename(title ='"pen')
	return filename
