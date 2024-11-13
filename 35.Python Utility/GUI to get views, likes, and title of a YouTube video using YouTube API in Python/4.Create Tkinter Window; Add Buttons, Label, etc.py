# Create Object
root = Tk()

# Set Geometry
root.geometry("500x300")

# Add Label, Entry Box and Button
Label(root, text="Title, Views, Likes of YouTube Video", fg="blue",
	font=("Helvetica 20 bold"), relief="solid", bg="white").pack(pady=10)
Label(root, text="Enter video URL or ID", font=("10")).pack()

video_url = Entry(root, width=40, font=("15"))
video_url.pack(pady=10)

Button(root, text="Get Details", font=("Helvetica 15 bold")).pack()

details = Label(root, text="")
details.pack(pady=10)

# Execute Tkinter
root.mainloop()
