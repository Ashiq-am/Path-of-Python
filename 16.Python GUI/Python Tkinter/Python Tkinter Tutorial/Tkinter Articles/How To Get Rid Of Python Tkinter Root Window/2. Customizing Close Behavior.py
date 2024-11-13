import tkinter as tk


def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root = tk.Tk()
root.title("Root Window")

# Create widgets and layout here

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
