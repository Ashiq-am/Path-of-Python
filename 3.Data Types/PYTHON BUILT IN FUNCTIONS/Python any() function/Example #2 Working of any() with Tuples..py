# All elements of tuple are true
t = (2, 4, 6)
print(any(t))

# All elements of tuple are false
t = (0, False, False)
print(any(t))

# Some elements of tuple are true while
# others are false
t = (5, 0, 3, 1, False)
print(any(t))

# Empty tuple
t = ()
print(any(t))
