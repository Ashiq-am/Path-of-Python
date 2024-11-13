from itertools import takewhile

# input string
st ="GeeksforGeeks"

# consider elements until
# 's' is encountered
li = list(takewhile(lambda x:x !='s', st))

print(li)
