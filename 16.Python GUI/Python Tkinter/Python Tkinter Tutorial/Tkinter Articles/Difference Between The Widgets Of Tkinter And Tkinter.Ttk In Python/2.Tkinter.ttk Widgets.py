import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter.Ttk Widgets Example")

# Create a label widget
label = ttk.Label(root, text="This is a Tkinter.Ttk Label")
label.pack()

# Create an entry widget
entry = ttk.Entry(root)
entry.pack()

# Create a button widget
button = ttk.Button(root, text="Click Me")
button.pack()

# Run the application
root.mainloop()
