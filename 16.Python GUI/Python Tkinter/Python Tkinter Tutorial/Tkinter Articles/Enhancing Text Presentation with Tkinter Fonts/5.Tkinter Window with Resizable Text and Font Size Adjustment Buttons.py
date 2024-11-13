import tkinter as tk
import tkinter.font as tkFont

def increase_font_size():
    font.config(size=font.actual()['size'] + 2)

def decrease_font_size():
    font.config(size=max(8, font.actual()['size'] - 2))  # Ensure font size doesn't go below 8

root = tk.Tk()
font = tkFont.Font(family="Times", size=12)
label = tk.Label(root, text="Resizable Text", font=font)
label.pack()

increase_button = tk.Button(root, text="Increase Font Size", command=increase_font_size)
increase_button.pack()

decrease_button = tk.Button(root, text="Decrease Font Size", command=decrease_font_size)
decrease_button.pack()

root.mainloop()
