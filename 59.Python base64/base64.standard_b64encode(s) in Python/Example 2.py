# import base64
from base64 import standard_b64encode

s = b'I love python'
# Using base64.standard_b64encode(s) method
gfg = standard_b64encode(s)

print(gfg)
