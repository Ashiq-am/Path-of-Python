# importing tkinter
import tkinter as tk

# function to run on pressing
# 'ENTER' key from keyboard.
def key_handler_function(event):
    label.config(text=entry.get())

# main application window
root = tk.Tk()
root.title("GeeksForGeeks")
root.geometry("300x200")

# creating widgets
entry = tk.Entry(root)
label = tk.Label(root, text="GeeksForGeeks")
entry.pack()
label.pack()


# Binding ENTER key to function
entry.bind("<Return>", key_handler_function)

# run the application
root.mainloop()
