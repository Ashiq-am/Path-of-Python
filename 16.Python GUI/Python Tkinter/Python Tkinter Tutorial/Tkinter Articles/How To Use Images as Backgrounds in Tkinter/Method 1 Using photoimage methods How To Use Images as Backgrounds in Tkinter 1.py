# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage( file = "Your_img.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

# Add text
label2 = Label( root, text = "Welcome",
			bg = "#88cffa")

label2.pack(pady = 50)

# Create Frame
frame1 = Frame( root, bg = "#88cffa")
frame1.pack(pady = 20)

# Add buttons
button1 = Button( frame1, text = "Exit")
button1.pack(pady = 20)

button2 = Button( frame1, text = "Start")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Reset")
button3.pack(pady = 20)

# Execute tkinter
root.mainloop()
