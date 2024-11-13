# import the product function from itertools module
from itertools import permutations

print("All the permutations of the given list is:")
print(list(permutations([1, 'geeks'], 2)))
print()

#Terminatingiterators


print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))
