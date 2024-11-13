# Python3 program to calculate Percentile of Students

# Function to calculate the percentile
def percentile(arr, n):
	i, j = 0, 0
	count, percent = 0, 0

	# Start of the loop that calculates percentile
	while i < n:

		count = 0
		j = 0
		while j < n:

			# Comparing the marks of student i
			# with all other students
			if (arr[i] > arr[j]):
				count += 1
			j += 1
		percent = (count * 100) // (n - 1)

		print("Percentile of Student ", i + 1," = ", percent)
		i += 1

# Driver Code

StudentMarks = [12, 60, 80, 71, 30]
n = len(StudentMarks)
percentile(StudentMarks, n)
