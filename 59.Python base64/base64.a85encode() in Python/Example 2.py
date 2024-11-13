# import base64
from base64 import a85encode

s = b'I love python'
# Using base64.a85encode() method
gfg = a85encode(s)

print(gfg)
