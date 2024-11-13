# import base64
from base64 import b32encode

s = b'I love python'
# Using base64.b32encode() method
gfg = b32encode(s)

print(gfg)
