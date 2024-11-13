img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()
