import tkinter as tk

def bring_to_front():
    root.focus_force()

root = tk.Tk()
root.title("Tkinter Window - focus_force")

button = tk.Button(root, text="Bring to Front", command=bring_to_front)
button.pack(pady=20)

root.mainloop()
