# importing tkinter
import tkinter as tk

# Function to update the image in label
def update_image_in_label():
    label_pic.config(image=image_2)

# tkinter application window
root = tk.Tk()
root.title("GeeksForGeeks")
root.geometry("400x200")
root.config(bg="green")

# Converting image to PhotoImage variables
image_1 = tk.PhotoImage(file="books_picture.png").subsample(2, 2)
image_2 = tk.PhotoImage(file="geeksforgeeks-logo.png")

# Label widget with image
label_pic = tk.Label(root, image=image_1)
label_pic.pack(pady=15)

# Button widget
update_button = tk.Button(root, text="Update image",
                          command=update_image_in_label,
                          bg="black", fg="white",
                          font=("Arial", 15))
update_button.pack()

# Run application
root.mainloop()
