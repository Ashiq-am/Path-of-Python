def open_file():
	file_path = filedialog.askopenfilename(
		title="Select a Text File", filetypes=[("Text files", "*.txt")])
	if file_path:
		with open(file_path, 'r') as file:
			content = file.read()
			text_widget.delete(1.0, tk.END) # Clear previous content
			text_widget.insert(tk.END, content)
