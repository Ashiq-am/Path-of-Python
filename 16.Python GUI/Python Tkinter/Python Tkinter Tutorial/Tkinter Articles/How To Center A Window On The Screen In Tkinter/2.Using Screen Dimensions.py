import tkinter as tk

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

# Example usage:
root = tk.Tk()
root.title("Centered Window")
center_window(root)
root.mainloop()
