# import base64
from base64 import b32decode
from base64 import b32encode

s = b'GeeksForGeeks'
s = b32encode(s)
# Using base64.b32decode() method
gfg = b32decode(s)

print(gfg)
