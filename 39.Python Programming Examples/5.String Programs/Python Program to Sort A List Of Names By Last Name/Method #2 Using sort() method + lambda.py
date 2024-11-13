# explicit function sort names
# by their surnames
def sortSur(nameList):
    # sort list by last name
    nameList.sort(key=lambda x: x.split()[-1])

    # return sorted list
    return nameList


# Driver Code

# assign list of names
nameList = ['John Wick', 'Jason Voorhees',
            'Freddy Krueger', 'Keyser Soze',
            'Mohinder Singh Pandher']

# display original list
print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))
