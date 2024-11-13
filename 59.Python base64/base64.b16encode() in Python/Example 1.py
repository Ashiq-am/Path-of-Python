# import base64
from base64 import b16encode

s = b'GeeksForGeeks'
# Using base64.b16encode() method
gfg = b16encode(s)

print(gfg)
