# import hashlib
import hashlib

# Using hashlib.sha3_512() method
gfg = hashlib.sha3_512()
gfg.update(b'GeeksForGeeks')

print(gfg.digest())
