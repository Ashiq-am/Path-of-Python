# import tkinter module
import tkinter as tk

# function to get text from entry widget
def print_entry_text():
    entry_text = entry.get()
    label.config(text=entry_text)

# main application window
root = tk.Tk()
root.title("Tkinter Entry Example")

# create entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# create button to display the content of entry widget
button = tk.Button(root, text="Print Text",
                   command=print_entry_text)
button.pack(pady=10)

# Create a Label widget to display the text
label = tk.Label(root, text="")
label.pack(pady=10)

# run the application
root.mainloop()
