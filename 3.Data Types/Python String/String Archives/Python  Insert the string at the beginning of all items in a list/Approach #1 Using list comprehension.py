# Python3 program to insert the string
# at the beginning of all items in a list
def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


# Driver function
list = [1, 2, 3, 4]
str = 'Geek'
print(prepend(list, str))
