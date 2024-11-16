# Let's define our function
# Parameters: Input Array
def sum(array):
    # Set variable for our final answer
    sum = 0

    # Parse through our array
    for i in array:
        # Continuously add current element
        # to final sum
        sum += i

    # Return our sum
    return sum


# Create a test array
testArray = [1, 3, 34, 92, 29, 48, 20.3]

# Test our function
print('The sum of your numbers is ' + str(sum(testArray)))
