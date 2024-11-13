list1 = [1]

# converting list to iterator
list_iter = iter(list1)

print(next(list_iter))
print(next(list_iter, "No more element"))
