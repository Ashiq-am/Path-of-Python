from tkinter import *
from tkinter.tix import *

# Create the main application window
root = Tk()
root.geometry("300x200")
root.title("Tooltip Example with Tix")

# Create a Balloon widget for tooltips
tool_tip = Balloon(root)

# Create a label widget
label1 = Label(root, text="Welcome to GeeksforGeeks")
label1.pack(pady=20)

# Create a button widget
button1 = Button(root, text="Click Me", bg="green", fg="white")
button1.pack(pady=10)

# Assign tooltips to the widgets
tool_tip.bind_widget(label1, balloonmsg="This is a Label")
tool_tip.bind_widget(button1, balloonmsg="This is a Button")

# Run the main application loop
root.mainloop()
