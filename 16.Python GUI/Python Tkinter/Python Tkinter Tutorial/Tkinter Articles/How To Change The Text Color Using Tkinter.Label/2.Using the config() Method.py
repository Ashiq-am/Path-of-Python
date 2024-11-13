import tkinter as tk

root = tk.Tk()
root.title("Change Text Color - Approach 2")

label = tk.Label(root, text="Hello GeeksforGeeks", font=("Helvetica", 16))
label.config(fg="green")
label.pack(pady=20)

root.mainloop()
