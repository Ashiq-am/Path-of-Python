# define the dictionary
dict1 = {}

# insert data into dictionary.
dict1 = {'NAME': ['Samuel', 'Richie', 'Lauren'],
         'AGE': [21, 20, 21],
         'COURSE': ['Data Structures', 'Machine Learning', 'OOPS with Java']}

# print the contents using zip format.
for each_row in zip(*([i] + (j)
                      for i, j in dict1.items())):
    print(*each_row, " ")
