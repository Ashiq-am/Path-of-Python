# Python3 program to find IQR of
# a data set

# Function to give index of the median
def median(a, l, r):
	n = r - l + 1
	n = (n + 1) // 2 - 1
	return n + l

# Function to calculate IQR
def IQR(a, n):

	a.sort()

	# Index of median of entire data
	mid_index = median(a, 0, n)

	# Median of first half
	Q1 = a[median(a, 0, mid_index)]

	# Median of second half
	Q3 = a[mid_index + median(a, mid_index + 1, n)]

	# IQR calculation
	return (Q3 - Q1)

# Driver Function
if __name__=='__main__':
	a = [1, 19, 7, 6, 5, 9, 12, 27, 18, 2, 15]
	n = len(a)
	print(IQR(a, n))
