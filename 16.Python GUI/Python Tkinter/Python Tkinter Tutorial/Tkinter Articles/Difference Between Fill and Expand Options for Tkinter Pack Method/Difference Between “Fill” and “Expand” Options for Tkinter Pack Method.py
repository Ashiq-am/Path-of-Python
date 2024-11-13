import tkinter as tk

root = tk.Tk()

# Creating widgets
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")

# Packing widgets
label1.pack(fill="both", expand=True)
label2.pack(fill="x")
label3.pack(fill="y")

root.mainloop()
