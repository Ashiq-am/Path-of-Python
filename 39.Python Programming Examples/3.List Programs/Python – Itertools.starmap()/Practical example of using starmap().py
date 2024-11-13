from itertools import starmap

co_ordinates = [(2, 3, 4),
                (3, 4, 5),
                (6, 8, 10),
                (1, 5, 7),
                (7, 4, 10)]

# Set true if coordinates form
# a right-triangle else false
right_triangles = list(starmap(lambda x, y, z: True
if ((x * x) + (y * y)) == (z * z)
else False, co_ordinates))

print("tuples which form right angled triangle :",
      right_triangles, end="\n\n")

print("The right triangle coordinates are :",
      end="")

# to print the coordinates
for i in range(0, len(right_triangles)):

    if right_triangles[i] == True:
        print(co_ordinates[i], end=" ")
