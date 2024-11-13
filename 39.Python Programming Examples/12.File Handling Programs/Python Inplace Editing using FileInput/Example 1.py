# Python code to change only first line of file
import fileinput

filename = "GFG.txt"

with fileinput.FileInput(filename,
						inplace = True, backup ='.bak') as f:

	for line in f:
		if f.isfirstline():
			print("changing only first line", end ='\n')
		else:
			print(line, end ='')
