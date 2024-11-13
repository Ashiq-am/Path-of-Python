# unpacking python tuple using _*

# first second and last value will be stored
# remaining will be ignored by using *_
a, b, *_, c = ("I ", "love ", "Geeks ",
			"for ", "Geeks ", 3000)

# print details
print(a)
print(b)
print(c)
