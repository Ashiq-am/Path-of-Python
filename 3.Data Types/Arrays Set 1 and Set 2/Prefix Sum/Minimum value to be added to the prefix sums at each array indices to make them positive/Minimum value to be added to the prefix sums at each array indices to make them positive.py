# Python3 program for the
# above approach

# Function to find minimum startValue
# for positive prefix sum at each index
def minStartValue(nums):
    # Store the minimum prefix sum
    minValue = 0

    # Stores prefix sum at each index
    sum = 0

    # Traverse over the array
    for i in range(len(nums)):
        # Update the prefix sum
        sum += nums[i]

        # Update the minValue
        minValue = min(minValue, sum)

    startValue = 1 - minValue

    # Return the positive start value
    return startValue


# Driver Code
if __name__ == '__main__':
    nums = [-3, 2, -3, 4, 2]

    # Function Call
    print(minStartValue(nums))
