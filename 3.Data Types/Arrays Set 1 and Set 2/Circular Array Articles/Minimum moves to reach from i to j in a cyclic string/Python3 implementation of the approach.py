# Python3 implementation of the approach

# Function to return the count of steps
# required to move from i to j
def getSteps(str, i, j, n):
    # Starting from i + 1
    k = i + 1

    # Count of steps
    steps = 0

    # Current character
    ch = str[i]
    while (k <= j):

        # If current character is different from previous
        if (str[k] != ch):
            # Increment steps
            steps = steps + 1

            # Update current character
            ch = str[k]

        k = k + 1

    # Return total steps
    return steps


# Function to return the minimum number of steps
# required to reach j from i
def getMinSteps(str, i, j, n):
    # Swap the values so that i <= j
    if (j < i):
        temp = i
        i = j
        j = temp

    # Steps to go from i to j (left to right)
    stepsToRight = getSteps(str, i, j, n)

    # While going from i to j (right to left)
    # First go from i to 0
    # then from (n - 1) to j
    stepsToLeft = getSteps(str, 0, i, n) + getSteps(str, j, n - 1, n)

    # If first and last character is different
    # then it'll add a step to stepsToLeft
    if (str[0] != str[n - 1]):
        stepsToLeft = stepsToLeft + 1

    # Return the minimum of two paths
    return min(stepsToLeft, stepsToRight)


# Driver code

str = "SSNSS"
n = len(str)
i = 0
j = 3
print(getMinSteps(str, i, j, n))
