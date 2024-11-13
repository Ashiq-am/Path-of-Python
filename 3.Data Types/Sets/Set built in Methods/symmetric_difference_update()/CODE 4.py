# Python code to demonstrate working of
# symmetric_difference_update()

A = {1, 2, 3, 4, 5}
B = [[1, 2, 3], 4, 5]

# error as b contain one element as list(unhashable object)

A.symmetric_difference_update(B)
print("A =", A)
