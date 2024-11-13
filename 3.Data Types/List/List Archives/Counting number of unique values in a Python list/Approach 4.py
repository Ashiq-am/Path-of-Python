# importing the module
import collections

# function to count the unique elements
def count_unique(my_list):

	# variable to store the unique count
	count = 0

	# creating dictionary to count frequency
	freq = collections.Counter(my_list)

	# traversing the dictionary
	for key, value in freq.items():
		if value == 1:
			count += 1

	# displaying the count of unique elements
	print(count)

# driver function
if __name__ == "__main__":

	my_list = [10, 20, 10, 30, 40, 40]
	count_unique(my_list)

	my_list = ['geeks', 'for', 'geeks']
	count_unique(my_list)
