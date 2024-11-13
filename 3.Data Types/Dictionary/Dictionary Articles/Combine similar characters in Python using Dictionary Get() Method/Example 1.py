# declaring the list of characters
mylist = ['g', 'e', 'e', 'k', 's', 'f',
          'o', 'r', 'g', 'e', 'e', 'k', 's']

# declaring the dictionary
dictionary = {}

# counting the frequency of the keys
for key in mylist:
    dictionary[key] = dictionary.get(key, 0) + 1

# storing the of keys and values
k = list(dictionary.keys())
v = list(dictionary.values())

# declaring the reslt list
result = []

# storing the product of keys and
# their respective values in result
for i, j in zip(k, v):
    result.append(i * j)

# displaying the result
print(result)
