def fibonacci_sequence(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci_sequence(50)

for value in fibonacci_gen:
    print(value)
