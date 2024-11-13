# Python code to implement the approach

# Function to find the minimum number
# of required groups
def minGroups(intervals):
    # Initilise a map to keep the
    # intervals in the sorted ordered
    # based on start ranges
    mp = [0] * 10001

    # Iterate over the each range of
    # ranges[] Increment the occurance
    # of interval in map
    for i in range(len(intervals)):
        mp[intervals[i][0]] = mp[intervals[i][0]] + 1
        mp[intervals[i][1] + 1] = mp[intervals[i][1] + 1] - 1

    # Initialise a varible result to
    # represents the maximum number of
    # intervals that overlap. Initialise
    # a variable sum to represents the
    # number of intervals that overlap
    # at a particular time
    result, sum = 0, 0

    # Iterate over the map and calcuate
    # the prefix sum of occurrence of
    # interval
    for it in range(len(mp)):
        # Maximise the result with maxium
        # number of intervals that overlap
        # at a particular time
        sum = sum + mp[it]
        result = max(result, sum)

    # Return the result
    return result


# Driver code
ranges = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]

# Function Call
print(minGroups(ranges))

# This code is contributed by Pushpesh Raj.
