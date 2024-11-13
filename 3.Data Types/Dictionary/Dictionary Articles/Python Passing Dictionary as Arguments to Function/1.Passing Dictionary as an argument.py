# Python program to demonstrate
# passing dictionary as argument


# A function that takes dictionary
# as an argument
def func(d):
    for key in d:
        print("key:", key, "Value:", d[key])

    # Driver's code


D = {'a': 1, 'b': 2, 'c': 3}
func(D)
