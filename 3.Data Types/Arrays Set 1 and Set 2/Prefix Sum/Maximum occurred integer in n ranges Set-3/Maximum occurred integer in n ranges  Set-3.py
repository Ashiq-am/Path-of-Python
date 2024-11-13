# Python 3 program of the above approach

# Function to print the most
# occurred element in given ranges
def maxOccurring(range1, n):
    # STL map for storing start
    # and end points
    points = {}

    for i in range(n):
        l = range1[i][0]
        r = range1[i][1]

        # Increment at starting point
        if l in points:
            points[l] += 1
        else:
            points[l] = 1

        # Decrement at ending point
        if r + 1 in points:
            points[r + 1] -= 1
        else:
            points[r + 1] = 0

    # Stores current frequency
    cur_freq = 0

    # Store element with maximum frequency
    ans = 0

    # Frequency of the current ans
    freq_ans = 0

    for key, value in points.items():
        # x.first denotes the current
        # point and x.second denotes
        # points[x.first]
        cur_freq += value

        # If frequency of x.first is
        # greater that freq_ans
        if (cur_freq > freq_ans):
            freq_ans = cur_freq
            ans = key

    # Print Answer
    print(ans)


# Driver code
if __name__ == '__main__':
    range1 = [[1, 6], [2, 3], [2, 5], [3, 8]]
    n = len(range1)

    # Function call
    maxOccurring(range1, n)

# This code is contributed by ipg2016107.
