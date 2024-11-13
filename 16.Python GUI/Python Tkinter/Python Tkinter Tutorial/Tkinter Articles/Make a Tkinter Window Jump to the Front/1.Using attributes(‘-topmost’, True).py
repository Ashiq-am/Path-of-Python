import tkinter as tk

def bring_to_front():
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)

root = tk.Tk()
root.title("Tkinter Window - Approach 1")
root.geometry("300x200")

button = tk.Button(root, text="Bring to Front", command=bring_to_front)
button.pack(pady=20)

root.mainloop()
