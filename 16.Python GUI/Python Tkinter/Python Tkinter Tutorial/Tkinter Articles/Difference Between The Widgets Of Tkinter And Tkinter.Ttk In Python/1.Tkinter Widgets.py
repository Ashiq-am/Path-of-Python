import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets Example")

# Create a label widget
label = tk.Label(root, text="This is a Tkinter Label")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button widget
button = tk.Button(root, text="Click Me")
button.pack()

# Run the application
root.mainloop()
