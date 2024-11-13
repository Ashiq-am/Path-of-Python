# Python program showing a use
# of lambda function

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# using map() function
squares = map(lambda x: x * x, nums)
print(list(squares))

# using filter() function
evens = filter(lambda x: True if (x % 2 == 0)
							else False, nums)
print(list(evens))
