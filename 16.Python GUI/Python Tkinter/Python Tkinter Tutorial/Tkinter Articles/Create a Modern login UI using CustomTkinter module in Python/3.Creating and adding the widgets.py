# Set the label
label = ctk.CTkLabel(app,text="This is the main UI page")

label.pack(pady=20)

# Create a frame
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,
		fill='both',expand=True)

# Set the label inside the frame
label = ctk.CTkLabel(master=frame,
					text='Modern Login System UI')
label.pack(pady=12,padx=10)

# Create the text box for taking
# username input from user
user_entry= ctk.CTkEntry(master=frame,
						placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

# Create a text box for taking
# password input from user
user_pass= ctk.CTkEntry(master=frame,
						placeholder_text="Password",
						show="*")
user_pass.pack(pady=12,padx=10)

# Create a login button to login
button = ctk.CTkButton(master=frame,
					text='Login',command=login)
button.pack(pady=12,padx=10)

# Create a remember me checkbox
checkbox = ctk.CTkCheckBox(master=frame,
						text='Remember Me')
checkbox.pack(pady=12,padx=10)

app.mainloop()
