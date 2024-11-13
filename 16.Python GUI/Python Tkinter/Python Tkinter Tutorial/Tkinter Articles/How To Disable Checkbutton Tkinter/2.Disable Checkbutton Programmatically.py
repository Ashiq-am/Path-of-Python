# import tkinter module
import tkinter as tk

# Function to disable the checkbutton 'chkbtn3' on clicking the button
def disable_checkbutton():
    # The checkbutton 'chkbtn3' is disabled now
    chkbtn3.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.geometry("300x150")
root.title("Disable Checkbutton Widget Example")

#  Create the CheckButton widget
chkbtn1 = tk.Checkbutton(root,text="Python")
chkbtn2 = tk.Checkbutton(root,text="Java")
chkbtn3 = tk.Checkbutton(root,text="C++")

chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

# Button to disable checkbutton on clicking this button
disable_Button = tk.Button(root,text="Disable",command=disable_checkbutton)
disable_Button.pack()

# Run the main event loop
root.mainloop()
