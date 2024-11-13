# Python code to demonstrate working of
# symmetric_difference_update()

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}

# result is always none.
result = A.symmetric_difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)
