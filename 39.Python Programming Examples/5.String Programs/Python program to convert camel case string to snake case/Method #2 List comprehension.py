# Python3 program to convert string
# from camel case to snake case

def change_case(str):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in str]).lstrip('_')


# Driver code
str = "GeeksForGeeks"
print(change_case(str))
