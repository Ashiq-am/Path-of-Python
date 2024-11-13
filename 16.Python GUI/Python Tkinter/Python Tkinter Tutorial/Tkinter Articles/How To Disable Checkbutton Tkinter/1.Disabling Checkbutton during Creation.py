# import tkinter module
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.geometry("400x200")
root.title("Disable Checkbutton Widget Example")

#  Create the CheckButton widget
chkbtn1 = tk.Checkbutton(root,text="Python")
chkbtn2 = tk.Checkbutton(root,text="Java")

# checkbutton disabled on creating.
chkbtn3 = tk.Checkbutton(root,text="C++", state=tk.DISABLED)

chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

# Run the main event loop
root.mainloop()
