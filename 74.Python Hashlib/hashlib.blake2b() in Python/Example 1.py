# import hashlib
import hashlib

# Using hashlib.blake2b() method
gfg = hashlib.blake2b()
gfg.update(b'GeeksForGeeks')

print(gfg.digest())
