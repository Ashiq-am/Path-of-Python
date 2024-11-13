import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Welcome to GeeksforGeeks")
label.pack(pady=20)

messages = [
    "Learn Data Structures",
    "Master Algorithms",
    "Explore Python",
    "Join Coding Contests",
    "Read Articles",
    "Practice Problems",
]
message_index = 0


def update_label():
    global message_index
    label.config(text=messages[message_index])
    message_index = (message_index + 1) % len(messages)
    root.after(2000, update_label)


def start_updates():
    update_label_button.config(state=tk.DISABLED)
    root.after(2000, update_label)


update_label_button = tk.Button(
    root, text="Start Updates", command=start_updates)
update_label_button.pack(pady=20)

root.mainloop()
