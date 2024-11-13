def upload_image():
	file_path = filedialog.askopenfilename()
	if file_path:
		image = Image.open(file_path)
		image.thumbnail((300, 300)) # Resize image if necessary
		photo = ImageTk.PhotoImage(image)
		image_label.config(image=photo)
		image_label.image = photo # Keep a reference to avoid garbage collection
		save_image(file_path)
		messagebox.showinfo("Success", "Image uploaded successfully!")
