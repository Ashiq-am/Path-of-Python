# Python3 program to convert
# list into a list of lists

def extractDigits(lst):
    return list(map(lambda el: [el], lst))


# Driver code
lst = ['alice', 'bob', 'cara']
print(extractDigits(lst))
