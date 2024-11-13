from tkinter import *

main = Tk()

# vriable for text
str_var = StringVar()

# Message Fucntion
label = Message( main, textvariable=str_var,
				relief=RAISED )

# The size of the text determines
# the size of the messagebox
str_var.set("You can't Change Your Profile Picture ")
label.pack()
main.mainloop()
