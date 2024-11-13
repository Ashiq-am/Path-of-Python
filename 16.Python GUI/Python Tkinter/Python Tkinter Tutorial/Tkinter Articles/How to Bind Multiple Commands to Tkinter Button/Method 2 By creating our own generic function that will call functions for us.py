# Import tkinter and Button Widget
from tkinter import Tk
from tkinter.ttk import Button

# funcs parameter will have the reference
# of all the functions that are passed as arguments i.e "fun1" and "fun2"
def combine_funcs(*funcs):

	# this function will call the passed functions
	# with the arguments that are passed to the functions
	def inner_combined_func(*args, **kwargs):
		for f in funcs:

			# Calling functions with arguments, if any
			f(*args, **kwargs)

	# returning the reference of inner_combined_func
	# this reference will have the called result of all
	# the functions that are passed to the combined_funcs
	return inner_combined_func

# Demo function 1
def fun1():
	print("Function 1")

# Demo function 2
def fun2():
	print("Function 2")

if __name__ == "__main__":
	# Creating top-level window
	master = Tk()

	# Setting window title
	master.title("Bind multiple function to Button")

	# Setting window Dimensions
	master.geometry("400x250")

	# Creating a button with more than one
	# command our own generic function
	button = Button(master, text="Button",
					command=combine_funcs(fun1, fun2))

	# Attaching button to the top-level window
	# Always remember to attach your widgets to the top-level
	button.pack()

	# Mainloop that will run forever
	master.mainloop()
