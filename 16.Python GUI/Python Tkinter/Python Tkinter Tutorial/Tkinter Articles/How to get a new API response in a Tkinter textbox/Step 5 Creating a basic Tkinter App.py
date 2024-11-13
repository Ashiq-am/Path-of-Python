import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button

root = tk.Tk()
root.title('Quoter')
text_box = Text(root, height=10, width=50)
get_button = Button(root, text="Get Quote", command=get_quote)

text_box.pack()
get_button.pack()
root.mainloop()
