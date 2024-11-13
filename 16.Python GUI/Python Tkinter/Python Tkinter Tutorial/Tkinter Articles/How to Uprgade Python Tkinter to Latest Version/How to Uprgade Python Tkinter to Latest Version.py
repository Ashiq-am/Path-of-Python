import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Pack the label widget into the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
