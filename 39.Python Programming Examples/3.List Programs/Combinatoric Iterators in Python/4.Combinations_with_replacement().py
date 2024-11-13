# import combinations from itertools module

from itertools import combinations_with_replacement

print ("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()

print ("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print ("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))
