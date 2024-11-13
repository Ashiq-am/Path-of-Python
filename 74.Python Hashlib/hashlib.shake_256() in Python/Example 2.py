# import hashlib
import hashlib

# Using hashlib.shake_256() method
gfg = hashlib.shake_256()
gfg.update(b'xyz@1234_GFG')

print(gfg.digest(15))
