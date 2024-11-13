# Python program to get
# dictionary keys as list

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


# Driver program
dict = {1: 'Geeks', 2: 'for', 3: 'geeks'}
print(getList(dict))
