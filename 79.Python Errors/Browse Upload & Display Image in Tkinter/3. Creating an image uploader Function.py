# image uploader function
def imageUploader():
	fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
	path = tk.filedialog.askopenfilename(filetypes=fileTypes)

	# if file is selected
	if len(path):
		img = Image.open(path)
		img = img.resize((200, 200))
		pic = ImageTk.PhotoImage(img)

		# re-sizing the app window in order to fit picture
		# and buttom
		app.geometry("560x300")
		label.config(image=pic)
		label.image = pic

	# if no file is selected, then we are displaying below message
	else:
		print("No file is chosen !! Please choose a file.")
