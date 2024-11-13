def create_input_page(self):
	for widget in self.winfo_children():
		widget.destroy()

	self.configure(bg="#90EE90")
	tk.Label(self, text="Enter a string:", bg="#90EE90",
			font=('Verdana', 16)).pack(pady=20)

	self.string_input = tk.Entry(self, font=("Calibri", 14))
	self.string_input.pack(pady=10)

	tk.Button(self, text="Check", bg="#FFFACD", font=(
		'sans-serif', 12), command=self.check_string).pack(pady=30)

	self.credits()
