# import modules
import tkinter as tk
from tkinter import messagebox

# function to check valid entry
def validate_not_empty(value):
    if value.strip():
        return True
    return False

# function called when Submit is clicked
def on_submit():
    value = entry.get()
    if not validate_not_empty(value):
        messagebox.showerror("Invalid Input",
                             "Field cannot be empty.")
    else:
        messagebox.showinfo("Valid Input",
                            "Input is valid.")

# main Tkinter application window
root = tk.Tk()
root.title("Empty Value Validation")
root.geometry("300x200")

# tkinter widgets
label = tk.Label(root, text="Enter something:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# sumit buttion to check validity
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
