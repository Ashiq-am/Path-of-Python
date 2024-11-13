# Python code to demonstrate working of
# symmetric_difference_update()

A = {1, 2, 3, 4, 5, 6}
B = [4, 5, 7, 8]

# passing argument as list

A.symmetric_difference_update(B)
print("A =", A)

A = {2, 4, 6, 8}
B = (i for i in range(2, 6))

# passing argument as generator object

A.symmetric_difference_update(B)
print("A=", A)
