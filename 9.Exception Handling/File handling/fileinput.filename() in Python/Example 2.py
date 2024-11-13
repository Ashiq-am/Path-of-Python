# import fileinput
import fileinput

# Using fileinput.input() method
for line in fileinput.input(files =('gfg.txt', 'gfg1.txt')):
	print(line)

print(fileinput.filename())
