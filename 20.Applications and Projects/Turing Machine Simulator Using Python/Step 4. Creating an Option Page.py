def create_options_page(self):
	for widget in self.winfo_children():
		widget.destroy()
		self.configure(bg="#ADD8E6")

		tk.Label(self, text="Select an option:", bg="#ADD8E6",
				font=('Verdana', 16)).pack(pady=20)

		options = [
		("String should accept odd one's and even zero's", 0),
		("String should accept even one's and odd zero's", 1),
			("String should accept even one's and even zero's", 2),
		("String should accept odd one's and odd zero's", 3)]
		self.selected_option = tk.IntVar()

		for option, value in options:
			tk.Radiobutton(self, text=option, bg="#ADD8E6", font=(
				'Verdana', 12),
					variable=self.selected_option,
					value=value).pack(pady=10)

			tk.Button(self, text="Next", bg="#FFFACD", font=(
				'sans-serif', 12),
				command=self.create_input_page).pack(pady=30)

			self.credits()
