# Python3 program to insert the string
# at the beginning of all items in a list
def prepend(List, str):
    # Using format()
    str += '{0}'
    List = ((map(str.format, List)))
    return List


# Driver function
list = [1, 2, 3, 4]
str = 'Geek'
print(prepend(list, str))
