# python code to implement the approach

# Function to find the difference between
# the sum of odd and even indexed elements
def helper(temp):
	oddSum = 0
	evenSum = 0
	for i in range(0, len(temp)):
		if (i % 2 == 0):
			evenSum += temp[i]
		else:
			oddSum += temp[i]

	return abs(evenSum - oddSum)

# Function to find the maximum possible difference
def maximumDiff(nums):
	temp = []
	val = 0
	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			for k in range(i, j+1):
				temp.append(nums[k])
			val = max(val, helper(temp))
			temp.clear()
	return val

# Driver Code
nums = [1, 2, 3, 4, -5]

# Function call
ans = maximumDiff(nums)
print(ans)

# This code is contributed by ksam24000
