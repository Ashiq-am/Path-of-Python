# Python3 Program to find depth of a dictionary
def dict_depth(dic, level=1):
    str_dic = str(dic)
    counter = 0
    for i in str_dic:
        if i == "{":
            counter += 1
    return (counter)


# Driver code
dic = {1: 'Geek', 2: {3: {4: {}}}}
print(dict_depth(dic))
