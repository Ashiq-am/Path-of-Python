# import modules
from tkinter import *
from urllib.request import urlopen, URLError

# user defined funtion
def URL_check():
	try:
		html = urlopen(str(e1.get()))
	except URLError as e:
		res = "Server not found!"
	else:
		res = "Server found"
	result.set(res)


# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()


# Creating label for each information

# name using widget Label
Label(master, text="Enter URL : ", bg="light grey").grid(row=1, sticky=W)
Label(master, text="Status :", bg="light grey").grid(row=3, sticky=W)

# Creating lebel for class variable

# name using widget Entry
Label(master, text="", textvariable=result,
	bg="light grey").grid(row=3, column=1, sticky=W)


e1 = Entry(master, width=50)
e1.grid(row=1, column=1)

# creating a button using the widget
b = Button(master, text="Check", command=URL_check, bg="white")
b.grid(row=1, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

mainloop()
