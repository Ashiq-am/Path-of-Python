# Python3 program to convert a list
# of integers into a single integer
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return (res)


# Driver code
list = [1, 2, 3]
print(convert(list))
