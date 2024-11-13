# import base64
from base64 import encodebytes
from base64 import decodebytes

s = b'GeeksForGeeks'
s = encodebytes(s)
# Using base64.decodebytes(s) method
gfg = decodebytes(s)

print(gfg)
