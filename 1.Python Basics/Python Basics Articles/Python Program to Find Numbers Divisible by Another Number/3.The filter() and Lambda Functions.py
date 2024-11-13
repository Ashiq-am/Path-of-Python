def find_divisibles(myList, num):
    # filter() and lambda functions
    return list(filter(lambda i: i % num == 0, myList))

myList = [8, 14, 21, 36, 43, 57, 63, 71, 83, 93]
num = 3
print(find_divisibles(myList, num))
