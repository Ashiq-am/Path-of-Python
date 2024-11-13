# Python code for the above approach

# Recursive function to return gcd of a and b
def __gcd(a, b):

	# Everything divides 0
	if (a == 0):
		return b;
	if (b == 0):
		return a;

	# base case
	if (a == b):
		return a;

	# a is greater
	if (a > b):
		return __gcd(a - b, b);
	return __gcd(a, b - a);

# Function to return total number of
# elements which are divisible by
# all their previous elements
def countElements(arr, N):
	ans = 0;
	lcm = arr[0];
	for i in range(1, N):

		# To check if number is divisible
		# by lcm of all previous elements
		if (arr[i] % lcm == 0):
			ans += 1

		# Updating LCM
		lcm = (lcm * arr[i]) / __gcd(lcm, arr[i]);
	return ans;

# Driver code
arr = [10, 6, 60, 120, 30, 360];

N = len(arr)
print(countElements(arr, N));

# This code is contributed by Saurabh Jaiswal
