# import hashlib
import hashlib

# Using hashlib.sha3_256() method
gfg = hashlib.sha3_256()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest())
