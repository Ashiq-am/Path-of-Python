import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("No Highlight Border Example")

    # Entry widget with no highlight border
    no_highlight_entry = tk.Entry(root, highlightthickness=0)
    no_highlight_entry.pack(padx=10, pady=10)

    root.mainloop()

create_window()
