s = "hello world"

# Use filter function with a lambda to create a new string
# by excluding characters that are 'o'
s = "".join(filter(lambda c: c != "o", s))
print(s)