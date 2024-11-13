import tkinter as tk


def close_window():
    root.destroy()


root = tk.Tk()
root.title("Root Window")

# Create widgets and layout here

close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.pack()

root.mainloop()
