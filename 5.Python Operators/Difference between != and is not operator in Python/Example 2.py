# Python3 code to
# illustrate the
# difference between
# != and is operator

a = 10
b = 10
print(a != b)
print(id(a), id(b))

c = "Python"
d = "Python"
print(c != d)
print(id(c), id(d))

e = [ 1, 2, 3, 4]
f=[ 1, 2, 3, 4]
print(e != f)
print(id(e), id(f))
