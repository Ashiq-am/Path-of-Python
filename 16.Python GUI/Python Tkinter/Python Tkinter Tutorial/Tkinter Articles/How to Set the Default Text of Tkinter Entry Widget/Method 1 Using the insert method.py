import tkinter as tk


root = tk.Tk()
root.geometry("200x100")

textBox = tk.Entry(root)
textBox.insert(0, "This is the default text")
textBox.pack()
root.mainloop()
