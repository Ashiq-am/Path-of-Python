import operator

# Example with a list
lst = [1, 2, 3, 4, 5]
print(operator.length_hint(lst))  # Output: 5

# Example with a generator
gen = (x for x in range(10))
print(operator.length_hint(gen))  # Output: 10
