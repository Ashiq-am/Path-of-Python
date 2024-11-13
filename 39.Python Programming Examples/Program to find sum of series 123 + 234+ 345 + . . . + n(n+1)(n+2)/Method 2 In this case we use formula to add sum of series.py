# Python program to find the
# sum of series
# 1*2*3 + 2*3*4 + . . .
# + n*(n+1)*(n+1)

# Function to calculate sum
# of series.
def sumOfSeries(n):
	return (n * (n + 1) * (n + 2
					) * (n + 3)) / 4

#Driver code
n = 10
print(sumOfSeries(n))
