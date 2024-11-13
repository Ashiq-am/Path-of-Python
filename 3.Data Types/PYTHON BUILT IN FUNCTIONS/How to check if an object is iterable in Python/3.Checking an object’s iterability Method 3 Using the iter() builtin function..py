# code
name = "Roster"

try:
    iter(name)
    print("{} is iterable".format(name))

except TypeError:
    print("{} is not iterable".format(name))
