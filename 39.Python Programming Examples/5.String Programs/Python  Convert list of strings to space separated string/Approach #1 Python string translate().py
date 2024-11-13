# Python3 program to Convert a list of
# strings to space-separated string

def convert(lst):
    return str(lst).translate(None, '[],\'')


# Driver code
lst = ['geeks', 'for', 'geeks']
print(convert(lst))
