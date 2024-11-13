# create two sample lists lst1 and lst2 as shown
lst1 = [10, 20, 30]
lst2 = [3, 4, 5]

# this empty list stores the output
result = []

# now, apply nested map function on both the
# created lists append the final output to
# the "result" list
list(map(lambda a: result.extend(map(a, lst2)),
		map(lambda a: lambda b: a+b, lst1)))

print(result)
