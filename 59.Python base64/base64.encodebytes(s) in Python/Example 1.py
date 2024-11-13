# import base64
from base64 import encodebytes

s = b'GeeksForGeeks'
# Using base64.encodebytes(s) method
gfg = encodebytes(s)

print(gfg)
