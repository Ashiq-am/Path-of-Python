# Importing tkinter
import tkinter as tk

# Function to replace image from Label
# on clicking the button 'replaceImageButton'
def replace_image():
    new_image = tk.PhotoImage(file="image_path")
    label1.config(image=new_image)
    label1.image = new_image

# GUI creation
root = tk.Tk()
root.geometry("300x200")
root.title("GeeksforGeeks")

# image is converted to PhotoImage variable
apple_picture = tk.PhotoImage(file="image_path")

# Label created with image
label1 = tk.Label(root, image=apple_picture)
label1.pack(pady=20)

# Create a button to replace the image
replaceImageButton = tk.Button(root,
                               text="Replace Image",
                               command=replace_image)
replaceImageButton.pack()

root.mainloop()
