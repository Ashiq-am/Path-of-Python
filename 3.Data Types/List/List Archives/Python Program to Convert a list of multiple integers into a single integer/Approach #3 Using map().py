# Python3 program to convert a list
# of integers into a single integer
def convert(list):
    # Converting integer list to string list
    # and joining the list using join()
    res = int("".join(map(str, list)))

    return res


# Driver code
list = [1, 2, 3]
print(convert(list))
