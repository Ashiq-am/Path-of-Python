# Python program to Remove all
# digits from a list of string
from string import digits


def remove(list):
    list = [''.join(x for x in i if x.isalpha()) for i in list]

    return list


# Driver code

list = ['4geeks', '3for', '4geeks']
print(remove(list))
