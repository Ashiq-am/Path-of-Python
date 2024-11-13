import tkinter as tk

root = tk.Tk()

# dimension of the GUI application
root.geometry("300x300")

# to make the GUI dimensions fixed
root.resizable(False, False)

# this is default entry box size
default_entry_box = tk.Entry(bg="blue", fg="white")
default_entry_box.pack()

# this is resized entry box with height 60
resizedHeight = tk.Entry(bg="green", fg="white")
resizedHeight.place(x=40, y=100, width=180, height=60)

root.mainloop()
