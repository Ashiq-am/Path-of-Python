# Here b is predefined and hence is optional.
def func(a, b=1098):
	return a+b


print(func(2, 2))

# this 1 is represented as 'a' in the function and
# function uses the default value of b
print(func(1))
