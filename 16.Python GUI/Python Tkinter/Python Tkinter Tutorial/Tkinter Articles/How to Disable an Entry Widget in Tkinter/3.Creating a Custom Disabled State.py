import tkinter as tk

def disable_entry(entry):
    entry.configure(state="disabled", disabledbackground="light gray")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

disable_entry(entry)

root.mainloop()
