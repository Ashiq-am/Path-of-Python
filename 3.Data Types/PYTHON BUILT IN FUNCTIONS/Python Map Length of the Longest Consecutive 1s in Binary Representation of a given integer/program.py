# Function to find Length of the Longest Consecutive
# 1's in Binary Representation

def maxConsecutive1(input):
	# convert number into it's binary
	input = bin(input)

	# remove first two characters of output string
	input = input[2:]

	# input.split('0') --> splits all sub-strings of
	# consecutive 1's separated by 0's, output will
	# be like ['11','1111']
	# map(len,input.split('0')) --> map function maps
	# len function on each sub-string of consecutive 1's
	# max() returns maximum element from a list
	print (max(map(len, input.split('0'))))

# Driver program
if __name__ == '__main__':
	input = 222
	maxConsecutive1(input)
