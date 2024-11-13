# Python code to convert list
# of string into list of list

# List initialization
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']

temp = []

# Getting elem in list of list format
for elem in Input:
    temp2 = elem.split(', ')
    temp.append((temp2))

# List initialization
Output = []

# Using Iteration to convert
# element into list of list
for elem in temp:
    temp3 = []
    for elem2 in elem:
        temp3.append(elem2)
    Output.append(temp3)

# printing
print(Output)
