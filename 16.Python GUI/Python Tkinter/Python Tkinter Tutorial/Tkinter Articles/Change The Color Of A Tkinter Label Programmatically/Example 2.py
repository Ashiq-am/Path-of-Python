# import tkinter module
import tkinter as tk

# Function to change the color of Label
# on clicking the button 'removeImageButton'
def remove_image():
    # Color of Label assigned a hex code
    label1.config(fg="#0A7A16")

# Create the main application window
root = tk.Tk()
root.geometry("300x150")
root.title("Changing Label Color Example")

# Label
label1 = tk.Label(root, text="Welcome to GFG",
                  font=("Times New Roman", 25, "bold"))
label1.pack(pady=20)

# Button to change the label color to green color.
removeImageButton = tk.Button(root, text="Change color",
                              command=remove_image,
                              bg="black", fg="white")
removeImageButton.pack()

# Run the main event loop
root.mainloop()
