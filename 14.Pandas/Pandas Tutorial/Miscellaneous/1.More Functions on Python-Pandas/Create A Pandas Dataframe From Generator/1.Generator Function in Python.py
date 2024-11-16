# A generator function that yields A for first time,
# B second time and C third time
def simple_generator():
    yield 'A'
    yield 'B'
    yield 'C'


# Driver code to check above generator function
for value in simple_generator():
    print(value)
