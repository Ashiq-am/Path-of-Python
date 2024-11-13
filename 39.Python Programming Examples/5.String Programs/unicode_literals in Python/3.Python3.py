# In python3
# By default the encoding is "utf-8"
import sys

# printing the default encoding
print("The default encoding for python3 is:", sys.getdefaultencoding())

# to define string as unicode
# we need to prefix every string with u"...."
p = u"\u2119"
y = u"\u01b4"
t = u"\u2602"
h = u"\u210c"
o = u"\u00f8"
n = u"\u1f24"

# printing Python
print(p+y+t+h+o+n)
