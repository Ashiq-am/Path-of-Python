# Python program to demonstrate
# slice() operator


# String slicing
String ='GeeksforGeeks'
s1 = slice(-3)
s2 = slice(-1, -5, -2)
print("String slicing")
print(String[s1])
print(String[s2])

# List slicing
L = [1, 2, 3, 4, 5]
s1 = slice(-3)
s2 = slice(-1, -5, -2)
print("\nList slicing")
print(L[s1])
print(L[s2])

# Tuple slicing
T = (1, 2, 3, 4, 5)
s1 = slice(-3)
s2 = slice(-1, -5, -2)
print("\nTuple slicing")
print(T[s1])
print(T[s2])
