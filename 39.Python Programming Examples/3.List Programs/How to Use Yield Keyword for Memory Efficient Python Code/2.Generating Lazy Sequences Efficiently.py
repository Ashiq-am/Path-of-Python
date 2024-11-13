def lazy_sequence(limit):
    for i in range(limit):
        yield i * 2

# Using the generator
gen = lazy_sequence(5)

for value in gen:
    print(value)
