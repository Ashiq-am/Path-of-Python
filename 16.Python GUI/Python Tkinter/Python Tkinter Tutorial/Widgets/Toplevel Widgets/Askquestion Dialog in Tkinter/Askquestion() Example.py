from tkinter import *
from tkinter import messagebox

# object of TK()
main = Tk()


# fucntion to use the
# askquestion() function
def Submit():
    messagebox.askquestion("Form","Do you want to Submit")


# setting geometry of window
# instance
main.geometry("100x100")

# creating Window
B1 = Button(main, text="Submit", command=Submit)

# Button positioning
B1.pack()

# infinte loop till close
main.mainloop()
