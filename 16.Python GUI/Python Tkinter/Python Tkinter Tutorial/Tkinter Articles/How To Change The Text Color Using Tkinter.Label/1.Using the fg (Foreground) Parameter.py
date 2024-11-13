import tkinter as tk

root = tk.Tk()
root.title("Change Text Color - Approach 1")

label = tk.Label(root, text="Hello GeeksforGeeks", fg="red", font=("Helvetica", 16))
label.pack(pady=20)

root.mainloop()
