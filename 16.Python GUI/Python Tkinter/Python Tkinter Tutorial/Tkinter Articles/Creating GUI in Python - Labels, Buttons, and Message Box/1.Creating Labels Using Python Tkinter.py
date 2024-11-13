import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Labels Example")

# Create a label
label = tk.Label(root, text="This is a label")
label.pack()

# Run the application
root.mainloop()
