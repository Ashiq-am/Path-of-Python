# import hashlib
import hashlib

# Using hashlib.blake2s() method
gfg = hashlib.blake2s()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest())
