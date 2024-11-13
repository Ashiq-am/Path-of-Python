# import base64
from base64 import urlsafe_b64encode

s = b'www.python.org / documentation'
# Using base64.urlsafe_b64encode(s) method
gfg = urlsafe_b64encode(s)

print(gfg)
