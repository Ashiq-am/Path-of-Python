# import base64
from base64 import encodebytes

s = b'I love python'
# Using base64.encodebytes(s) method
gfg = encodebytes(s)

print(gfg)
