# Python code to check for identifiers
def Count(string):
    print("Length before strip()")
    print(len(string))

    # Using strip() to remove white spaces
    str = string.strip()
    print("Length after removing spaces")
    return str


# Driver Code
string = " Geeks for Geeks "
print(len(Count(string)))
