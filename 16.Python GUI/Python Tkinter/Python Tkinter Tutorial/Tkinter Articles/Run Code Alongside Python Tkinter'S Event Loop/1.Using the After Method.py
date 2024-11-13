import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="", font=("Helvetica", 14))
label.pack(pady=20)

counter = 1

def update_label():
    global counter
    if counter <= 10:
        print(counter)
        label.config(text=str(counter))
        counter += 1
        root.after(1000, update_label)

root.after(1000, update_label)

root.mainloop()
