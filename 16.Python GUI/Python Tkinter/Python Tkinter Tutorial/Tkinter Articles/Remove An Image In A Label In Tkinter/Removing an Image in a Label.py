# Importing tkinter
import tkinter as tk

# Function to remove image from Label
# on clicking the button 'removeImageButton'.

def remove_image():
    label1.config(image="")

# GUI creation
root = tk.Tk()
root.geometry("300x200")
root.title("GeeksforGeeks")

# image is converted to PhotoImage variable
apple_picture = tk.PhotoImage(file="image_path")

# Label created with image
label1 = tk.Label(root, image=apple_picture)
label1.pack(pady=20)

# Button created to remove the image
# from the Label widget 'label1'
removeImageButton = tk.Button(
    root, text="Remove image",
    command=remove_image,
    bg="green", fg="white")
removeImageButton.pack()
root.mainloop()
