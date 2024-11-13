# Python program to find the
# sum of series
# 1*2*3 + 2*3*4 + . . .
# + n*(n+1)*(n+1)

# Function to calculate sum
# of series.
def sumOfSeries(n):
	sum = 0
	i = 1
	while i<=n:
		sum = sum + i * (i + 1) * (
								i + 2)
		i = i + 1
	return sum

# Driver code
n = 10
print(sumOfSeries(n)) 
