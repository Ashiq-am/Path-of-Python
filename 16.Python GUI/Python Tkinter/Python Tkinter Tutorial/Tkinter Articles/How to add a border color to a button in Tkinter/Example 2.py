from tkinter import *

window = Tk()
window.geometry('250x150')
window.title('Button Widget')

# Button with black border
border = LabelFrame(window, bd = 6, bg = "black")
border.pack(pady = 10)

btn = Button(border, text="Button", width = 8,
			bg = "#6CD300", fg = "black")
btn.pack()

window.mainloop()
