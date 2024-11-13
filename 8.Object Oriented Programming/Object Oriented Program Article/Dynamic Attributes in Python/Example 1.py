class GFG:
    None


def value():
    return 10


# Driver Code
g = GFG()

# Dynamic attribute of a
# class object
g.d1 = value

# Dynamic attribute of a
# function
value.d1 = "Geeks"

print(value.d1)
print(g.d1() == value())
