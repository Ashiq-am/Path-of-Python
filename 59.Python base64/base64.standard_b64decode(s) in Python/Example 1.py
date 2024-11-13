# import base64
from base64 import standard_b64decode
from base64 import standard_b64encode

s = b'GeeksForGeeks'
s = standard_b64encode(s)
# Using base64.standard_b64decode() method
gfg = standard_b64decode(s)

print(gfg)
