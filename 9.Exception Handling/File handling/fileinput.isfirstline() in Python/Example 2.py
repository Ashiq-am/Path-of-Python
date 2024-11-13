# import fileinput
import fileinput

# Using fileinput.isfirstline() method
for line in fileinput.input(files =('gfg.txt', 'gfg1.txt')):
	print(fileinput.isfirstline())
