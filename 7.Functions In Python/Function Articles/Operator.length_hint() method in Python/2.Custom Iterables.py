import operator

class CustomIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    def __length_hint__(self):
        return self.end - self.start + 1

# Usage
custom_iter = CustomIterable(1, 10)
print(operator.length_hint(custom_iter))  # Output: 10
