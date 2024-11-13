def select_file():
	global file_names
	file_names = askopenfilenames(initialdir = "/",title = "Select File")

# IMAGE TO PDF
def image_to_pdf():
	for index, file_name in enumerate(file_names):
		with open(f"file {index}.pdf", "wb") as f:
			f.write(img2pdf.convert(file_name))

# IMAGES TO PDF
def images_to_pdf():
	with open(f"file.pdf","wb") as f:
		f.write(img2pdf.convert(file_names))
