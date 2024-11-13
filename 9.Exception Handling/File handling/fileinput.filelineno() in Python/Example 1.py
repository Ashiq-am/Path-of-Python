# import fileinput
import fileinput

# Using fileinput.filelineno() method
for line in fileinput.input(files ='gfg.txt'):
	print('{}. '.format(fileinput.filelineno()) + line)
