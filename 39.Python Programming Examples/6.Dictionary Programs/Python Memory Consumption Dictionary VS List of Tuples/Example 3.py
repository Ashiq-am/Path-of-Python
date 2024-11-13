import sys

# for dict
dict = {}
for i in range(1, 101):
	dict[i] = i
print(dict)
print(sys.getsizeof(dict))

# for list of tuples
lst = list(range(1, 101))
print(lst)
print(sys.getsizeof(lst))
