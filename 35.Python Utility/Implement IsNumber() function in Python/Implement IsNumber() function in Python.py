# Implementation of isNumber() function
def isNumber(s):
    # handle for negative values
    negative = False
    if (s[0] == '-'):
        negative = True

    if negative == True:
        s = s[1:]

    # try to convert the string to int
    try:
        n = int(s)
        return True
    # catch exception if cannot be converted
    except ValueError:
        return False


s1 = "9748513"
s2 = "-9748513"
s3 = "GeeksforGeeks"

print("For input '{}' isNumber() returned : {}".format(s1, isNumber(s1)))
print("For input '{}' isNumber() returned : {}".format(s2, isNumber(s2)))
print("For input '{}' isNumber() returned : {}".format(s3, isNumber(s3)))
