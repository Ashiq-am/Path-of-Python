# import modules
import tkinter as tk
from tkinter import messagebox
import re

# function to check valid email
def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, email):
        return True
    return False

# function called when Submit is clicked
def on_submit():
    email = email_entry.get()
    if not validate_email(email):
        messagebox.showerror("Invalid Input",
                             "Email must contain '@' and '.' characters.")
    else:
        messagebox.showinfo("Valid Input", "Email is valid.")

# main Tkinter application window
root = tk.Tk()
root.title("Email Validation")
root.geometry("300x200")

# tkinter widgets
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# sumit buttion to check validity
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
