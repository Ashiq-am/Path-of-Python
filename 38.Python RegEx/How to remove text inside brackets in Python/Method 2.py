# Input string
string = "geeks(for)geeks"

# resultant string
result = ''

# paren counts the number of brackets encountered
paren = 0
for ch in string:

    # if the character is ( then increment the paren
    # and add ( to the resultant string.
    if ch == '(':
        paren = paren + 1
        result = result + '('

    # if the character is ) and paren is greater than 0,
    # then increment the paren and
    # add ) to the resultant string.
    elif (ch == ')') and paren:
        result = result + ')'
        paren = paren - 1

    # if the character neither ( nor then add it to
    # resultant string.
    elif not paren:
        result += ch

# print the resultant string.
print(result)
