from collections import Counter

# List initialization
Input1 = [1, 2, 3]
Input2 = [2, 1, 2, 1, 3, 5, 2, 3]


temp = Counter(Input2)
Output = sum(temp[x] for x in Input1)

# Printing output
print("Initial list are:", Input1, Input2)
print("Frequency is:", Output)
