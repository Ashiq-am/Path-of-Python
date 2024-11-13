# import hashlib
import hashlib

# Using hashlib.shake_128() method
gfg = hashlib.shake_128()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest(15))
