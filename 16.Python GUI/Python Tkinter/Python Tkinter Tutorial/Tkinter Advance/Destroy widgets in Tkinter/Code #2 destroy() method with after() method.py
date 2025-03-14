# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Creating button. In this destroy method is passed
# as command, so as soon as button 1 is pressed root
# window will be destroyed
btn1 = Button(root, text ="Button 1")
btn1.pack(pady = 10)

# Creating button. In this destroy method is passed
# as command, so as soon as button 2 is pressed
# button 1 will be destroyed
btn2 = Button(root, text ="Button 2")
btn2.pack(pady = 10)

# after method destroying button-1
# and button-2 after certain time
btn1.after(3000, btn1.destroy)
btn2.after(6000, btn2.destroy)

# infinite loop
mainloop()
