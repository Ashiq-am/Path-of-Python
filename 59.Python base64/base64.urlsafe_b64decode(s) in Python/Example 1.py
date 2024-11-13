# import base64
from base64 import urlsafe_b64decode
from base64 import urlsafe_b64encode

s = b'GeeksForGeeks'
s = urlsafe_b64encode(s)
# Using base64.urlsafe_b64decode() method
gfg = urlsafe_b64decode(s)

print(gfg)
