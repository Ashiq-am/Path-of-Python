def los(l):
    res = []

    for i in l:
        # creating an empty set
        x = set()
        x.add(i)
        res.append(x)

    # returning final list of sets
    return (res)


# Driver code
lst = {'sky', 'is', 'blue'}

# Printing the final result
print(los(lst))
