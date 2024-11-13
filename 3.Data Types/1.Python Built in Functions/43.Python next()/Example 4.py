l_iter = iter([1, 2])

print("Next Item:", next(l_iter))
print("Next Item:", next(l_iter))

# this line should raise StopIteration exception
print("Next Item:", next(l_iter))
