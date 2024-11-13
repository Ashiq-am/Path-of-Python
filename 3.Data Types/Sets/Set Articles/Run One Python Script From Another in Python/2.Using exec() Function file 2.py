# file_2.py

# opening file_1.py and reading it with read() and executing if with exec()
with open("file_1.py") as file:
	exec(file.read())
