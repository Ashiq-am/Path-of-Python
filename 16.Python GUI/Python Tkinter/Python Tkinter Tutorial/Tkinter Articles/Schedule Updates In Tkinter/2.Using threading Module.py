import tkinter as tk
import threading
import time

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Welcome to GeeksforGeeks", width=30, height=2, font=("Helvetica", 16))
label.pack(pady=20)

colors = [
    ("red", "white"),
    ("green", "black"),
    ("blue", "yellow"),
    ("yellow", "blue"),
    ("purple", "white"),
    ("orange", "black")
]
color_index = 0

def update_color():
    global color_index
    while True:
        time.sleep(2)
        bg_color, fg_color = colors[color_index]
        root.after(0, lambda: label.config(bg=bg_color, fg=fg_color))
        color_index = (color_index + 1) % len(colors)

def start_updates():
    update_label_button.config(state=tk.DISABLED)
    thread = threading.Thread(target=update_color, daemon=True)
    thread.start()

update_label_button = tk.Button(root, text="Start Updates", command=start_updates, font=("Helvetica", 14))
update_label_button.pack(pady=20)

root.mainloop()
