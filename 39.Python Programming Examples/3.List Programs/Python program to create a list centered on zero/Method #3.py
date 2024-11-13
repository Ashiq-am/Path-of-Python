# Python3 Python program to create a list centered on zero

def create(limit, diff):
    length = int(((limit / diff) * 2) + 1)
    list = [-limit + i * diff for i in range(length)]
    return list


# Driver code
limit = 1
diff = 0.5
print(create(limit, diff))
