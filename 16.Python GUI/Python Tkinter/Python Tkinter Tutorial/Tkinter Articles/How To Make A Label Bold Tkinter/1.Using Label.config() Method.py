import tkinter as tk
root = tk.Tk()
root.title("Bold Label Example1 ")
label = tk.Label(root, text="Hello GFG - Message 1 ")
label.config(font=("Helvetica", 12, "bold"))
label.pack(pady=20)
root.mainloop()
