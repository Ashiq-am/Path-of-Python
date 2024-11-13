import tkinter as tk
from tkinter import Frame, Label
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image in Frame Example")
root.geometry("400x400")  # Optional: set window size

# Create a frame within the main window
frame = Frame(root, width=300, height=300, bg="white")
frame.pack(pady=20)  # Adjust padding as necessary

# Load the image using Pillow
image_path = "C:\\Users\\HP\\Desktop\\Folder1\\geeksforgeeks.png"  # Replace with your image path
image = Image.open(image_path)

# Resize the image using the new resampling attribute
image = image.resize((250, 250), Image.Resampling.LANCZOS)

# Convert the image to a Tkinter-compatible photo image
photo_image = ImageTk.PhotoImage(image)

# Create a label widget to hold the image
image_label = Label(frame, image=photo_image)

# Place the label in the frame
image_label.pack()

# Run the Tkinter event loop
root.mainloop()
