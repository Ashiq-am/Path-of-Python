# Import required module
import random
import array



# Create class to shuffle array
class Shuffler(object):

	# Constructor
	def __init__(self, arr):

		# Initializes the temp_array
		self.temp_array = arr

		# All the indices are stored in indices list
		self.indices = [index for index in range(len(arr))]

	# method to shuffle array
	def shuffle(self):

		# if length of array is zero empty array is returned.
		if not len(self.temp_array):
			return []

		# The below swapping process is repeated randomly in range of
		# half of length of array to length of the array, in this case,
		# it is repeated randomly in between 3 to 6 times.
		for i in range(random.randint(int(len(self.temp_array)/2), len(self.temp_array))):

			# randomly choses two indices that is i, j from indices list
			i = random.choice(self.indices)
			j = random.choice(self.indices)

			# swapping the elements present at i,j indices.
			self.temp_array[i], self.temp_array[j] = self.temp_array[j], self.temp_array[i]
		return self.temp_array



# Driver code

# Assign array
arr = array.array('q', [1, 2, 3, 4, 5, 6])

# Create Object of Shuffler class
ob = Shuffler(arr)

# Display original array
print("Original array: ", arr)

# Shuffle method is called
print("Shuffled array: ", ob.shuffle())
