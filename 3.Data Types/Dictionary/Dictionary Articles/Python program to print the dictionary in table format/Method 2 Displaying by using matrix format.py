# define the dictionary
dict1 = {}

# insert data into dictionary
dict1 = {(0, 0): 'Samuel', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'Richie', (1, 1): 20, (1, 2): 'Machine Learning',
         (2, 0): 'Lauren', (2, 1): 21, (2, 2): 'OOPS with Java'
         }

# print the name of the columns explicitly.
print(" NAME ", " AGE ", " COURSE ")

# Iterate through the dictionary
# to print the data.
for i in range(3):

    for j in range(3):
        print(dict1[(i, j)], end=' ')

    print()
