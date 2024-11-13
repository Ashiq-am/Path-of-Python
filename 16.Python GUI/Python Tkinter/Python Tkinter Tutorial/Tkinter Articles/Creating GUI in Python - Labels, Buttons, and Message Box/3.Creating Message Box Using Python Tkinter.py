import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, this is a message!")

# Create the main application window
root = tk.Tk()
root.title("Message Box Example")

# Create a button to trigger the message box
button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

# Run the application
root.mainloop()
