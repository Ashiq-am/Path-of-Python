# Python3 program to convert string
# from camel case to snake case

def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)


# Driver code
str = "GeeksForGeeks"
print(change_case(str))
