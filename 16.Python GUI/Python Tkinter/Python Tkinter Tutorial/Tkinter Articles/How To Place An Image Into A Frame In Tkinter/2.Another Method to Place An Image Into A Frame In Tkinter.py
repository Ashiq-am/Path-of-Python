import tkinter as tk
from tkinter import Frame, Canvas
from PIL import Image, ImageTk

# Step 1: Initialize the main window
root = tk.Tk()
root.title("Image in Frame Example")

# Step 2: Create a frame within the main window
frame = Frame(root, width=400, height=400)
frame.pack()

# Step 3: Load the image using PIL
image_path = "C:\\Users\\HP\\Desktop\\python programming gnitc\\geeksforgeeks.png"   # Replace with your image path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Step 4: Create a Canvas widget and add the image to it
canvas = Canvas(frame, width=500, height=400)
canvas.pack()

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Keep a reference to avoid garbage collection
canvas.image = photo

# Start the main loop
root.mainloop()
