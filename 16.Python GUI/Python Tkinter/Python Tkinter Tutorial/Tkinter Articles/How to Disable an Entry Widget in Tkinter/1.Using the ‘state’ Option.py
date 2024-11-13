import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.config(state="disabled")
entry.pack()

root.mainloop()
