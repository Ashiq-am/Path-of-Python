class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current


# Create an instance of FibonacciIterator
fib_iterator = FibonacciIterator(100)

# Using a for loop to iterate
print("Using for loop:")
for num in fib_iterator:
    print(num)

# Using next() to iterate
print("\nUsing next() function:")
fib_iterator = FibonacciIterator(100)
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
print(next(fib_iterator))
