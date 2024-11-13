# create a list of 10 elements
data = [10, 2, 3, 4, 56, 32, 56, 32, 21, 59]

# apply a filter that takes only even numbers with
# lambda as predicate
a = filter(lambda x: x % 2 == 0, data)

# display
for i in a:
	print(i)

print("------------")


# apply a filter that takes only odd numbers with
# lambda as predicate
a = filter(lambda x: x % 2 != 0, data)

# display
for i in a:
	print(i)
