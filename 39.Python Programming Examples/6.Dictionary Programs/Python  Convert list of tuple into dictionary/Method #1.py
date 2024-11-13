# Python code to convert list of tuple into dictionary showing
# relation of every element from first list to every other element in the list.

# List initialization
indices = ['x', 'y', 'z', 'w', 't', 'r']
relation = [('x', 'y'), ('x', 'z'), ('x', 'w'), ('y', 'z'), ('y', 'w'), ('z', 'w')]

# dictionary initialization
Output = {}

# Iteration
for elem in indices:
    temp = []
    for rel in relation:
        if elem in rel:
            if elem == rel[0]:
                temp.append(rel[1])
            else:
                temp.append(rel[0])

    Output[elem] = temp
    temp = []

print("Initial list of tuple is :")
print(relation)
print("Converted dictionary of list :")
print(Output)
