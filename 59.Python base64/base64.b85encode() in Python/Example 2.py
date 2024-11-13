# import base64
from base64 import b85encode

s = b'I love python'
# Using base64.b85encode() method
gfg = b85encode(s)

print(gfg)
