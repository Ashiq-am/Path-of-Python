# Import module
import tkinter
import tkinter.font

# Creating the GUI window.
root = tkinter.Tk()
root.title("Welcome to GeekForGeeks")
root.geometry("918x450")

# Creating our text widget.
sample_text=tkinter.Text( root, height = 10)
sample_text.pack()

# Create an object of type Font from tkinter.
Desired_font = tkinter.font.Font( family = "Comic Sans MS",
								size = 20,
								weight = "bold")

# Parsed the Font object
# to the Text widget using .configure( ) method.
sample_text.configure(font = Desired_font)
root.mainloop()
