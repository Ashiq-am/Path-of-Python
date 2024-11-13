# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.

# Input list initialisation
Input1 = [10, 20, 30, 40, 50, 60]
Input2 = [60, 50, 40, 30, 20, 10]

# Output list initialisation
Output = [Input1[i]-Input2[i] if Input1[i] > Input2[i] \
		else Input1[i] for i in range(len(Input1))]

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)
