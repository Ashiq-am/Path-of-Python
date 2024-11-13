import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter UI")

# Ensure correct parent widget
label = tk.Label(root, text="Hello, Tkinter!", master=root)

root.mainloop()  # Start the Tkinter event loop
