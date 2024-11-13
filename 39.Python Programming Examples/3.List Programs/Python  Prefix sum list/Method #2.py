# function to find cumulative sum of list
from itertools import accumulate

def cumulativeSum(lst):
	print (list(accumulate(lst)))

# Driver program
if __name__ == "__main__":
	lst = [3, 4, 1, 7, 9, 1]
	cumulativeSum(lst)
