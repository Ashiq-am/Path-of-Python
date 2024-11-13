# import base64
from base64 import b85decode
from base64 import b85encode

s = b'Hello World'
s = b85encode(s)
# Using base64.b85decode() method
gfg = b85decode(s)

print(gfg)
