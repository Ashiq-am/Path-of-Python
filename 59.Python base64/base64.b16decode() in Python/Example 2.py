# import base64
from base64 import b16decode
from base64 import b16encode

s = b'Hello World'
s = b16encode(s)
# Using base64.b16decode() method
gfg = b16decode(s)

print(gfg)
