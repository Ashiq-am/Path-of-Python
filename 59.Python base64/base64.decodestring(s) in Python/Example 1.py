# import base64
from base64 import encodestring
from base64 import decodestring

s = b'GeeksForGeeks'
s = encodestring(s)
# Using base64.decodestring(s) method
gfg = decodestring(s)

print(gfg)