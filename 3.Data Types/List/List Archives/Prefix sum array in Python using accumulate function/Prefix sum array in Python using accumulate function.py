# function to find cumulative sum of array
from itertools import accumulate

def cumulativeSum(input):
	print ("Sum :", list(accumulate(input)))

# Driver program
if __name__ == "__main__":
	input = [4, 6, 12]
	cumulativeSum(input)
