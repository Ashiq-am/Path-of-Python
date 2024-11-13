# Python program to demonstrate
# truncate method using with statement

with open('file1.txt', 'w') as fp:
	fp.truncate(50)
