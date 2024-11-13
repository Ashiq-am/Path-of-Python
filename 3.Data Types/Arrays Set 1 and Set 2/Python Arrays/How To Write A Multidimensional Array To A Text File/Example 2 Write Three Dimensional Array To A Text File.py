# Define the dimensions of the array
first_dimension = 2
second_dimension = 3
third_dimension = 4

# Initialize the three-dimensional array with zeros
three_dimensional_array = [[[0 for _ in range(third_dimension)]
                            for _ in range(second_dimension)]
                           for _ in range(first_dimension)]

# Fill the array with values
value = 1
for i in range(first_dimension):
    for j in range(second_dimension):
        for k in range(third_dimension):
            three_dimensional_array[i][j][k] = value
            value += 1

# Open a file for writing
with open("output.txt", "w") as file:
    # Write the three-dimensional array to the file
    for i in range(first_dimension):
        for j in range(second_dimension):
            for k in range(third_dimension):
                file.write(f"{three_dimensional_array[i][j][k]} ")

            file.write("\n")

        file.write("\n")

# Print a message
print("\nOutput Written to output.txt")
