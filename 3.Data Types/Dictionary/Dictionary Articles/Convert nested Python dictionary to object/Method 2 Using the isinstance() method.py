def dict2obj(d):
    # checking whether object d is a
    # instance of class list
    if isinstance(d, list):
        d = [dict2obj(x) for x in d]

    # if d is not a instance of dict then
    # directly object is returned
    if not isinstance(d, dict):
        return d

    # declaring a class
    class C:
        pass

    # constructor of the class passed to obj
    obj = C()

    for k in d:
        obj.__dict__[k] = dict2obj(d[k])

    return obj


# initializing the dictionary
dictionary = {'A': 1, 'B': {'C': 2},
              'D': ['E', {'F': 3}], 'G': 4}

# calling the function dict2obj and
# passing the dictionary as argument
obj2 = dict2obj(dictionary)

# accessing the dictionary as an object
print(obj2.A)
print(obj2.B.C)
print(obj2.D[0])
print(obj2.D[1].F)
print(obj2.G)
