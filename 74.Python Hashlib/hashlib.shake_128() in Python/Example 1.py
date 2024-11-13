# import hashlib
import hashlib

# Using hashlib.shake_128() method
gfg = hashlib.shake_128()
gfg.update(b'GeeksForGeeks')

print(gfg.digest(10))
