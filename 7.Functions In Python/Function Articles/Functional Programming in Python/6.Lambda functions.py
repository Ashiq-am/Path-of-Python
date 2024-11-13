# Python code to demonstrate
# lambda


cube = lambda x: x * x * x
print(cube(7))

L = [1, 3, 2, 4, 5, 6]
is_even = [x for x in L if x % 2 == 0]

print(is_even)
