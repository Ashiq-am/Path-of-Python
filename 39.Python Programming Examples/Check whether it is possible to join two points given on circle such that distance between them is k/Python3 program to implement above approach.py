# Python3 program to implement above approach
from math import sqrt, ceil, floor


# Return distance between the centers
def dis(x1, y1, x2, y2):
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def check(c1, c2, k):
    min = 0
    max = 0

    # Distance between centers
    de = dis(c1[0], c1[1], c2[0], c2[1])

    # Case 5
    if (de == 0):

        # SubCase 1
        if (c1[2] == c2[2]):
            min = 0
            max = 0

        # Subcase 2
        else:
            if (c1[2] - c2[2] > 0):
                min = c1[2] - c2[2]
                max = min + 2 * c2[2]

            else:
                min = c2[2] - c1[2]
                max = min + 2 * c1[2]

            # Case 1
    elif (de >= c1[2] + c2[2]):
        min = de - c1[2] - c2[2]
        max = de + c1[2] + c2[2]

    # Case 3
    elif (de + c2[2] < c1[2]):
        max = c2[2] + c1[2] + de
        min = c1[2] - de - c2[2]

    # Case 4
    elif (de + c1[2] < c2[2]):

        max = c2[2] + c1[2] + de
        min = c2[2] - de - c1[2]

    # Case 2
    elif ((de + c2[2] >= c1[2]) or (de + c1[2] >= c2[2])):
        max = c2[2] + c1[2] + de
        min = 0

    # Since value of k wialways be an integer
    temin = ceil(min)
    re = max
    if (k >= temin and k <= re):
        return True
    return False


# Driver Code
circle1 = [0, 0, 5]
circle2 = [8, 3, 2]
k = 3

if (check(circle1, circle2, k)):
    print("YES")
else:
    print("NO")
