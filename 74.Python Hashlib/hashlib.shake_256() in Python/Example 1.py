# import hashlib
import hashlib

# Using hashlib.shake_256() method
gfg = hashlib.shake_256()
gfg.update(b'GeeksForGeeks')

print(gfg.digest(10))
