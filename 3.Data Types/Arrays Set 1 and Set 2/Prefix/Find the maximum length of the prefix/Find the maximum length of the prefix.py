# Python3 implementation of the approach

# Function to return the maximum
# length of the required prefix
def Maximum_Length(a):

	# Array to store the frequency
	# of each element of the array
	counts =[0]*11

	# Iterating for all the elements
	for index, v in enumerate(a):

		# Update the frequency of the
		# current element i.e. v
		counts[v] += 1

		# Sorted positive values from counts array
		k = sorted([i for i in counts if i])

		# If current prefix satisfies
		# the given conditions
		if len(k)== 1 or (k[0]== k[-2] and k[-1]-k[-2]== 1) or (k[0]== 1 and k[1]== k[-1]):
			ans = index

	# Return the maximum length
	return ans + 1

# Driver code
if __name__=="__main__":
	a = [1, 1, 1, 2, 2, 2]
	n = len(a)
	print(Maximum_Length(a))
