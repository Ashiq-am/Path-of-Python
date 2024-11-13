# Import library
import tkinter as tk

# Create top level window
frame = tk.Tk()
frame.title("Text Cursor")
frame.geometry('200x200')

# Create Text widget with "red" text cursor
inputtxt = tk.Text(frame, height=5, width=20,
				insertbackground="red")
inputtxt.place(x=20, y=20)

frame.mainloop()
