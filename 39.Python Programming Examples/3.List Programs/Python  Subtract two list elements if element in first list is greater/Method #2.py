# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.

# Input list initialisation
Input1 = [10, 20, 30, 40, 50, 60]
Input2 = [60, 50, 40, 30, 20, 10]

# using zip()
Output =[e1-e2 if e1>e2 else e1 for (e1, e2) in zip(Input1, Input2)]

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)
