import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# initialize style function
style = ttk.Style()

# Use clam theme
style.theme_use('clam')

# Used TLabelframe for styling labelframe widgets,
# and use red color for border
style.configure("TLabelframe", bordercolor="red")

labelframe = ttk.LabelFrame(root, text = "GFG")
labelframe.grid(padx = 30, pady = 30)

left = tk.Label(labelframe, text = "Geeks for Geeks")
left.pack()

root.mainloop()
