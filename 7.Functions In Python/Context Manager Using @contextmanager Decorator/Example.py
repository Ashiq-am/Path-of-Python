# Python program to demonstrate
# Context Manager

with open('testfile.txt') as in_file:
	print(''.join(in_file.readlines()))
