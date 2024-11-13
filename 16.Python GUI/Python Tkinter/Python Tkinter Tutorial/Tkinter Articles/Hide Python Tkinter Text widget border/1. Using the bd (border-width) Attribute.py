import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("No Border Example")

    # Button with no border
    no_border_button = tk.Button(root, text="No Border", bd=0)
    no_border_button.pack(padx=10, pady=10)

    root.mainloop()

create_window()
