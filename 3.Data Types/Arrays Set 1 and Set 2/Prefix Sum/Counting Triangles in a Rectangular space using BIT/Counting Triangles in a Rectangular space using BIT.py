# A Python3 program implementing
# the above queries
maxn = 2005

# 2D Binary Indexed Tree.
# Note: global variable
# will have initially all
# elements zero
bit = [[0 for j in range(maxn)]
       for i in range(maxn)]


# function to add a point
# at(x, y)
def update(x, y):
    y1 = 0
    while (x < maxn):

        # x is the xth BIT that will
        # be updated while y is the
        # indices where an update
        # will be made in xth BIT
        y1 = y

        while (y1 < maxn):
            bit[x][y1] += 1
            y1 += (y1 & -y1)

        # next BIT that should
        # be updated
        x += x & -x


# Function to return number of
# points in the rectangle(1, 1),
# (x, y)
def query(x, y):
    res = 0
    y1 = 0

    while (x > 0):

        # xth BIT's yth node must
        # be added to the result
        y1 = y

        while (y1 > 0):
            res += bit[x][y1]
            y1 -= y1 & -y1

        # next BIT that will contribute
        # to the result
        x -= x & -x

    return res


# (x1, y1) is the lower left
# and (x2, y2) is the upper
# right corner of the rectangle
def pointsInRectangle(x1, y1,
                      x2, y2):
    # Returns number of points
    # in the rectangle (x1, y1),
    # (x2, y2) as described in
    # text above
    return (query(x2, y2) - query(x1 - 1, y2) -
            query(x2, y1 - 1) + query(x1 - 1, y1 - 1))


# Returns count of triangles with
# n points, i.e., it returns nC3
def findTriangles(n):
    # returns pts choose 3
    return ((n * (n - 1) *
             (n - 2)) // 6)


# Driver code
if __name__ == "__main__":
    # inserting points
    update(2, 2)
    update(3, 5)
    update(4, 2)
    update(4, 5)
    update(5, 4)

    print("No. of triangles in the " +
          "rectangle (1, 1) (6, 6) are: ",
          findTriangles(pointsInRectangle(1, 1,
                                          6, 6)))
    update(3, 3)
    print("No. of triangles in the rectangle " + "(1, 1) (6, 6) are:", findTriangles(pointsInRectangle(1, 1, 6, 6)))
