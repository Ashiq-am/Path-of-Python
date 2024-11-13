"""

"""


"""Below is the python implementation of the idea discussed above. Let’s suppose the name of the 
script is print_my_name."""



# Python program to prints it own name upon execution
import sys

def main():
	program = sys.argv[0] # argv[0] contains the full path of the file

	# rfind() finds the last index of backslash
	# since in a file path the filename comes after the last '\'
	index = program.rfind("\\") + 1

	# slicing the filename out of the file path
	program = program[index:]
	print("Program Name: % s" % program)

# executes main
if __name__ == "__main__":
	main()
