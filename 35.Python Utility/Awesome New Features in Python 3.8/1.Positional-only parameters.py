# Arguments before / are considered
# as positional arguments only
def add(x, y, /, z = 0):
	a = x + y + z
	return a

# Driver's code
print(add(2, 5))
print(add(2, 5, 7))
print(add(x = 2, y = 5))
