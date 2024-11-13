# if you enter number n it will automatically
# be considered as a square matrix of size n by n
size_of_a_matrix = int(input("Enter size the matrix that you want : "))

if size_of_a_matrix <= 3:
    # since size should be greater than 3
    print("Please enter the size that is greater than 3")
    exit()

diagonal = []
numbers1 = [[0 for j in range(0, size_of_a_matrix)]
            for i in range(0, size_of_a_matrix)]

# created a loop to enter numbers
for a in range(size_of_a_matrix):
    numbers1 = int(input(f"Enter the numbers for the main diagonal for position[{a}][{a}] : "))

    # appending the values to the list
    diagonal.append(numbers1)

diagonalAbove = []
print("*********")

# created a loop to enter numbers
for k in range(size_of_a_matrix - 1):
    numbers2 = int(input(f"Enter the numbers for diagonal above the main diagonal for position[{k}][{k + 1}]: "))

    # appending the values to the list
    diagonalAbove.append(numbers2)

diagonalBelow = []
print("*********")

# created a loop to enter numbers
for z in range(size_of_a_matrix - 1):
    numbers3 = int(input(f"Enter the numbers for diagonal below the main diagonal for position[{z + 1}][{z}]: "))

    # appending the values to the list
    diagonalBelow.append(numbers3)
print("*********")


def tridiagonal(size_of_a_matrix, diagonal, diagonalAbove, diagonalBelow):
    matrix = [[0 for j in range(size_of_a_matrix)]
              for i in range(size_of_a_matrix)]

    for k in range(size_of_a_matrix - 1):
        matrix[k][k] = diagonal[k]
        matrix[k][k + 1] = diagonalAbove[k]
        matrix[k + 1][k] = diagonalBelow[k]

    matrix[size_of_a_matrix - 1][size_of_a_matrix - 1] = diagonal[size_of_a_matrix - 1]

    # so that the values will print row by row
    for row in matrix:
        print(row)

    return "this is the tridiagonal matrix"


# printing final values
print(tridiagonal(size_of_a_matrix, diagonal, diagonalAbove, diagonalBelow))
