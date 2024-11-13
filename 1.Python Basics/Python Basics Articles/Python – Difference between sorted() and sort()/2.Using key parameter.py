# Python program to demonstrate
# sorted()


L = ['aaaa', 'bbb', 'cc', 'd']

# sorted without key parameter
print(sorted(L))
print()

# sorted with key parameter
print(sorted(L, key = len))
