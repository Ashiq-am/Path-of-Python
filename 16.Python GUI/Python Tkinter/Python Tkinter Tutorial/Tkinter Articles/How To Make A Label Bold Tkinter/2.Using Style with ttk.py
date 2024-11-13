import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Bold Example 2")
style = ttk.Style()
style.configure("Bold.TLabel", font=("Helvetica", 12, "bold"))
label = ttk.Label(root, text="Hello GFG - Example 2", style="Bold.TLabel")
label.pack(pady=20)
root.mainloop()
