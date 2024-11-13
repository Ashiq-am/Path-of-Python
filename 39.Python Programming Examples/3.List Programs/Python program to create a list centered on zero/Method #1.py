# Python3 program to Convert a
# list to dictionary

def create(limit, diff):
    lst = [-limit]
    while lst[-1] < limit:
        lst.append(lst[-1] + diff)
    lst[-1] = limit
    return lst


# Driver code
limit = 1
diff = 0.5
print(create(limit, diff))
