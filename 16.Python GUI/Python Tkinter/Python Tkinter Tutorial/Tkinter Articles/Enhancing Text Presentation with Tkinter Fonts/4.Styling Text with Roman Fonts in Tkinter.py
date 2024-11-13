import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

# Create fonts with different weights and slants
roman_font = tkFont.Font(family="Arial", size=12, slant=tkFont.ROMAN)

# Create labels using font styles
label = tk.Label(root, text="Roman Text", font=roman_font)
label.pack()

root.mainloop()
