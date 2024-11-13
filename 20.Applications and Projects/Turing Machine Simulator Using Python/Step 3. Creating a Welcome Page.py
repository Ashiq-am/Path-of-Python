def create_welcome_page(self):
	self.configure(bg="#1E90FF")

	tk.Label(self, text="Turing Machine Simulator",
			bg="#1E90FF", fg="white",
			font=('Helvetica', 32, "bold")).pack(pady=50)

	tk.Button(self,
			text="Get Started",
			bg="#FFFACD",
			font=('sans-serif', 22, "bold"),
			command=self.create_options_page).pack(pady=50)

	self.credits()
