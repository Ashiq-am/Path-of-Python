# Program to Reverse an array
# upto a given position

def reverseArrayUptoK(input, k):

	# reverse list starting from k-1 position
	# and split remaining list after k
	# concat both parts and print
	# input[k-1::-1] --> generate list starting
	# from k-1 position element till first
	# element in reverse order
	print (input[k-1::-1] + input[k:])

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 4, 5, 6]
	k = 4
	reverseArrayUptoK(input, k)
