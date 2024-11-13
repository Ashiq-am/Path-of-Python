# Import Module
from tkinter import *

# Create Objects
root = Tk()

# Buttons
Button(root, relief=RAISED, bitmap="error").pack(pady=10)
Button(root, relief=RAISED, bitmap="hourglass").pack(pady=10)
Button(root, relief=RAISED, bitmap="info").pack(pady=10)
Button(root, relief=RAISED, bitmap="question").pack(pady=10)
Button(root, relief=RAISED, bitmap="warning").pack(pady=10)
Button(root, relief=RAISED, bitmap="gray75").pack(pady=10)
Button(root, relief=RAISED, bitmap="gray50").pack(pady=10)
Button(root, relief=RAISED, bitmap="gray25").pack(pady=10)
Button(root, relief=RAISED, bitmap="gray12").pack(pady=10)
Button(root, relief=RAISED, bitmap="questhead").pack(pady=10)

# Execute Tkinter
root.mainloop()
