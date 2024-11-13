# Python code to implement the above approach

# Define a class called CircularHiding


class CircularHiding:

	# Define a method called hide that
	# takes four arguments
	def hide(self, n, k, l, m):

		# Create an empty set to store
		# occupied hiding spots
		occupied_spots = set()

		# Initialize a variable to count
		# the number of collisions
		collisions = 0

		# Loop through the range of numbers
		# from 0 to N-1
		for i in range(n):

			# Calculate the hiding spot
			# based on the formula given
			P = (k * i*i + l * i + m) % n

			# If the hiding spot is already
			# occupied, find the next
			# available spot
			while P in occupied_spots:
				collisions += 1
				P = (P + 1) % n

			# Add the new hiding
			# spot to the occupied set
			occupied_spots.add(P)

		# Return the total number
		# of collisions
		return collisions


# Create an instance of the
# CircularHiding class
ch = CircularHiding()

# Call the hide method with the
# given parameters and store the
# result in the collisions variable
collisions = ch.hide(67, 2, 9, 7)

# Print the total number of
# collisions
print(collisions)
