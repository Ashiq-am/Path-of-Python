# import fileinput
import fileinput

# Using fileinput.lineno() method
for line in fileinput.input(files ='gfg.txt'):
	print('{}. '.format(fileinput.lineno()) + line)
