# import hashlib
import hashlib

# Using hashlib.sha3_512() method
gfg = hashlib.sha3_512()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest())
