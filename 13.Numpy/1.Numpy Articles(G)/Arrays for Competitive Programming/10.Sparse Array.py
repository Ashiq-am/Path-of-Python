# Implementation of array representation
# of the sparse array

# Define the sparse array
sparse = [
    [0, 0, 7, 0],
    [1, 0, 0, 0],
    [2, 0, 5, 0],
    [0, 8, 0, 4]
]

# Initialize a variable to count non-zero elements
s = 0
for i in range(4):
    for j in range(4):
        if sparse[i][j] != 0:
            s += 1

# Create a 2D array to represent the sparse array
representsparse = [[0] * s for _ in range(3)]

# Populate the representation array
k = 0
for i in range(4):
    for j in range(4):
        if sparse[i][j] != 0:
            representsparse[0][k] = i
            representsparse[1][k] = j
            representsparse[2][k] = sparse[i][j]
            k += 1

# Display the representation of the sparse array
print("Representation of Sparse array using arrays:\n")
for i in range(3):
    if i == 0:
        print("row: ", end="")
    elif i == 1:
        print("column: ", end="")
    else:
        print("value: ", end="")

    for j in range(s):
        print(" ", representsparse[i][j], end="")

    print()
