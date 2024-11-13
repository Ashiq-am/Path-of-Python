# Python3 program to convert
# list into a list of lists

def extractDigits(lst):
    return [[el] for el in lst]


# Driver code
lst = ['alice', 'bob', 'cara']
print(extractDigits(lst))
