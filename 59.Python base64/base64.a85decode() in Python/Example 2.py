# import base64
from base64 import a85decode
from base64 import a85encode

s = b'Hello World'
s = a85encode(s)
# Using base64.a85decode() method
gfg = a85decode(s)

print(gfg)
