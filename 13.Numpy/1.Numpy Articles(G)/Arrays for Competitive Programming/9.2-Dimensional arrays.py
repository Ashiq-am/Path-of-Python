n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

TwoDList = []

# Initialize the list of lists
for i in range(n):
    TwoDList.append([])

# Taking input in the list of lists
for i in range(n):
    for j in range(m):
        value = int(input("Enter value for position ({}, {}): ".format(i, j)))
        TwoDList[i].append(value)
