import tkinter as tk

root = tk.Tk()

# dimension of the GUI application
root.geometry("300x300")

# to make the GUI dimensions fixed
root.resizable(False, False)

# increase font size to increase height of entry box
using_font_resize = tk.Entry(font=("arial", 24), fg="white", bg="black")
using_font_resize.pack()

root.mainloop()
