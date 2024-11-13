# Python3 program for the above approach

# Function to find the total of the
# seats booked in each of the flights
def corpFlightBookings(Bookings, N):

	# Stores the resultant sequence
	res = [0] * N

	# Traverse the array
	for i in range(len(Bookings)):

		# Store the first booked flight
		l = Bookings[i][0]

		# Store the last booked flight
		r = Bookings[i][1]

		# Store the total number of
		# seats booked in flights [l, r]
		K = Bookings[i][2]

		# Add K to the flight L
		res[l - 1] = res[l - 1] + K

		# Subtract K from flight
		# number R + 1
		if (r <= len(res) - 1):
			res[r] = (-K) + res[r]

	# Find the prefix sum of the array
	for i in range(1, len(res)):
		res[i] = res[i] + res[i - 1]

	# Prthe total number of seats
	# booked in each flight
	for i in range(len(res)):
		print(res[i], end = " ")

# Driver Code
if __name__ == '__main__':

	# Given list of bookings
	bookings = [ [ 1, 3, 100 ],
			[ 2, 6, 100 ],
			[ 3, 4, 100 ] ]
	N = 6

	# Function Call
	corpFlightBookings(bookings, N)
