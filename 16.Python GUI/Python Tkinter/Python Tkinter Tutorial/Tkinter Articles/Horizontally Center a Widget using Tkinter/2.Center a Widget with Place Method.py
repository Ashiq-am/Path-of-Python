import tkinter as tk  # Import the Tkinter library

# Create the main application window
root = tk.Tk()
root.geometry('400x300')  # Set the window size to 400x300 pixels

# Create a label widget with text and background color
label = tk.Label(root, text="Centered Label", bg="lightblue")

root.update_idletasks()  # Ensure the window dimensions are updated
label.update_idletasks()  # Ensure the label dimensions are updated

# Get the width of the window and the label widget
window_width = root.winfo_width()
widget_width = label.winfo_width()

# Calculate the x-coordinate to center the label horizontally
x = (window_width - widget_width) // 2

# Place the label at the calculated x-coordinate and a fixed y-coordinate
label.place(x=x, y=100)

# Run the Tkinter event loop to display the window
root.mainloop()
