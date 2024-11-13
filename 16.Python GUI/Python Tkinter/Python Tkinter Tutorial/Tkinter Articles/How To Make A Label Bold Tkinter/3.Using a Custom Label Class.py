import tkinter as tk
from tkinter import font

class BoldLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        bold_font = font.Font(self, self.cget("font"))
        bold_font.configure(weight="bold")
        self.configure(font=bold_font)

root = tk.Tk()
root.title("Bold Label Example 3")

label = BoldLabel(root, text="Hello GFG - Example 3", font=("Helvetica", 12))
label.pack(pady=20)

root.mainloop()
