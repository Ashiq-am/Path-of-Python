# import combinations from itertools module

from itertools import combinations

print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print ("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()

print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2),1)))
