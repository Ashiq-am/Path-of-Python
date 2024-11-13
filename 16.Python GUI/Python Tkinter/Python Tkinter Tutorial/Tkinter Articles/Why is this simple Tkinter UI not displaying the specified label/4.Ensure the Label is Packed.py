import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter UI")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()  # Ensure the label is packed

root.mainloop()
