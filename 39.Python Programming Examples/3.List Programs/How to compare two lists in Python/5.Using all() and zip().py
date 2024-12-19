a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

# Use the all() function along with zip() to
#compare both lists element by element
res = all(x == y for x, y in zip(a, b))
print(res)