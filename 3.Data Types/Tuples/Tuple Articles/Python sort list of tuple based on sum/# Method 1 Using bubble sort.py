# Python code to sort list of tuple based on sum of element in tuple.

# Input list initialisation
Input = [(4, 5), (2, 3), (6, 7), (2, 8)]

print("The original list of tuple is ")
print(Input)

# getting length of list of tuples
lst = len(Input)

# Bubble sort
for i in range(lst):

    for j in range(lst - i - 1):
        if (Input[j][0] + Input[j][1]) > (Input[j + 1][0] + Input[j + 1][1]):
            Input[j], Input[j + 1] = Input[j + 1], Input[j]

        # print output
print("\nThe answer is")
print(Input)
