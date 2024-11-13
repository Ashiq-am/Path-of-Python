# import base64
from base64 import b32encode

s = b'GeeksForGeeks'
# Using base64.b32encode() method
gfg = b32encode(s)

print(gfg)
