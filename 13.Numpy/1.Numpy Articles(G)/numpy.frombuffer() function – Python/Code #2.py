# Python program explaining
# numpy.frombuffer() function

# importing numpy as geek
import numpy as geek

gfg = geek.frombuffer(b'\x01\x02\x03\x04\x05\x06\x07', dtype=geek.uint8, count=5)

print(gfg)
