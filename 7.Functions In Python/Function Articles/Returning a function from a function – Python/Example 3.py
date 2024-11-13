# first method that return second method
def A(u, v):
    w = u + v
    z = u - v

    # return second method without name
    return lambda: print(w * z)


# form a object of first method
# i.e; second method
returned_function = A(5, 2)

# check object
print(returned_function)

# call second method by first method
returned_function()
