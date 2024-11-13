# Python program to find an index which has
# same number of even elements on left and
# right, Or same number of odd elements on
# left and right.
class pair:
    def __init__(self, f, s):
        self.first = f
        self.second = s


# Function to Find index
def Find_Index(n, arr):
    odd, even = 0, 0

    # Create two vectors of pair type
    v_left = []
    v_right = []

    v_left.append(pair(odd, even))
    for i in range(n - 1):

        if (arr[i] % 2 == 0):
            even += 1

        else:
            odd += 1

        v_left.append(pair(odd, even))

    odd = 0
    even = 0
    v_right.append(pair(odd, even))
    for i in range(n - 1, 0, -1):
        if (arr[i] % 2 == 0):
            even += 1
        else:
            odd += 1

        v_right.append(pair(odd, even))

    v_right = v_right[::-1]

    for i in range(len(v_left)):

        # To check even or odd of Both sides are
        # equal or not
        if (v_left[i].first == v_right[i].first or v_left[i].second == v_right[i].second):
            return i

    return -1


# Driver code
arr = [4, 3, 2, 1, 2]
n = len(arr)
index = Find_Index(n, arr)
if (index == -1):
    print("-1")
else:
    print("index = " + str(index))

# This code is contributed by shinjanpatra
