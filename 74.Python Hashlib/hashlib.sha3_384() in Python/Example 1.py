# import hashlib
import hashlib

# Using hashlib.sha3_384() method
gfg = hashlib.sha3_384()
gfg.update(b'GeeksForGeeks')

print(gfg.digest())
