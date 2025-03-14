# Python3 code to find sum of
# Manhattan distance between all
# the pairs of given points

# Return the sum of distance
# between all the pair of points.
def distancesum(x, y, n):
    sum = 0

    # for each point, finding distance
    # to rest of the point
    for i in range(n):
        for j in range(i + 1, n):
            sum += (abs(x[i] - x[j]) +
                    abs(y[i] - y[j]))

    return sum


# Driven Code
x = [-1, 1, 3, 2]
y = [5, 6, 5, 3]
n = len(x)
print(distancesum(x, y, n))
