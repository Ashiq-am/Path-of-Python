# import hashlib
import hashlib

# Using hashlib.sha3_224() method
gfg = hashlib.sha3_224()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest())
