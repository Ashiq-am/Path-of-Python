import tkinter as tk  # Import the Tkinter library

# Create the main application window
root = tk.Tk()
root.geometry('400x300')  # Set the window size to 400x300 pixels

# Create a label widget with text and background color
label = tk.Label(root, text="Centered Label", bg="lightblue")

# Pack the label widget to the top of the window, center it
# horizontally, and add padding in the y-direction
label.pack(side='top', anchor='center', pady=100)

# Run the Tkinter event loop to display the window
root.mainloop()
