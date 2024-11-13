import tkinter as tk

def text_only(entered_data):
	return entered_data.isalpha()

root = tk.Tk()

# the dimensions of the GUI window
root.geometry("300x300")
root.resizable(False, False) # fixed size for GUI

# create a function and pass in register
# the function is to check the validation of Tkinter Box
valid = root.register(text_only), '%S'
entry_box = tk.Entry(validate="key", validatecommand=valid)
entry_box.pack()

# end GUI window with root.mainloop()
root.mainloop()
