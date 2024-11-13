import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter UI")

label = tk.Label(root, text="Hello, Tkinter!")  # Ensure correct parent widget
label.pack()  # Ensure the label is packed

root.mainloop()  # Start the Tkinter event loop
