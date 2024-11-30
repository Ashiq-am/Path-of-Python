import numpy as np

# Input number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Empty list to hold the rows
data = []

# Input each row
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split()))
    data.append(row)

# Convert list of lists to NumPy array
arr = np.array(data)
print("2D NumPy Array:")
print(arr)