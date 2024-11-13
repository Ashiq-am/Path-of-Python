import tkinter as tk


def non_removable_text(text):
    # Enter Your Name is non-removable Text
    return text.startswith("Enter Your Name:")


root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)

# define a function with non-removable text
# '%P' denotes the value that the text will
# have if the change is allowed.
valid = root.register(non_removable_text), "%P"

# create a Entry widget with a validate of key
# key-specify keystroke
entry = tk.Entry(validate='key', validatecommand=(valid))

# add a message
entry.insert("end", "Enter Your Name:")
entry.place(x=0, y=100, width=300)

root.mainloop()
