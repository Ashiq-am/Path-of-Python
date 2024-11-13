# unpacking python tuple using _

# first and last value will be ignored
# and won't be stored second will be
# assigned to b and remaining will be
# assigned to x
_, b, *x, _ = ("I ", "love ", "Geeks ",
			"for ", "Geeks ", 3000)

# print details
print(b)
print(x)
