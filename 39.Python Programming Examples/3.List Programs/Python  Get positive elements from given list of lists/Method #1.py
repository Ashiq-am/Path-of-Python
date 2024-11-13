# Python code to get positive
# element from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]
Output = []

# Using iteration
for elem in Input:
    temp = []
    for x in elem:
        if x > 0:
            temp.append(x)
    Output.append(temp)

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)
