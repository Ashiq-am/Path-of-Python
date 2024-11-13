import tkinter as tk
import threading
import time

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="", font=("Helvetica", 14))
label.pack(pady=20)

combinations = [
    "GeeksforGeeks",
    "Geeksfor",
    "Geeks",
    "forGeeks",
    "GfG",
    "GeeksforGeeks Rocks",
    "Learn at GeeksforGeeks",
    "GeeksforGeeks Python",
    "GeeksforGeeks Algorithms",
    "GeeksforGeeks Data Structures"
]
combination_index = 0

def run_in_thread():
    global combination_index
    while combination_index < len(combinations):
        print(combinations[combination_index])
        root.after(0, lambda: label.config(text=combinations[combination_index]))
        combination_index += 1
        time.sleep(1)

thread = threading.Thread(target=run_in_thread, daemon=True)
thread.start()

root.mainloop()
