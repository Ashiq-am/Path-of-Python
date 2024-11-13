# Python3 program to Convert single
# indexed list into multiple indexed list

def convert(lst):
    return ([i for item in lst for i in item.split()])


# Driver code
lst = ['Geeksforgeeks is a portal for geeks']
print(convert(lst))
