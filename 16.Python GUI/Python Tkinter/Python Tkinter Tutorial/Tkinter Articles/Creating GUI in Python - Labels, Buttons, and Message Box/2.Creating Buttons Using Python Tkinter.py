import tkinter as tk

def button_click():
    print("Button clicked")

# Create the main application window
root = tk.Tk()
root.title("Buttons Example")

# Create a button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Run the application
root.mainloop()
