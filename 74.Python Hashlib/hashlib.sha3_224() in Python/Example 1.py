# import hashlib
import hashlib

# Using hashlib.sha3_224() method
gfg = hashlib.sha3_224()
gfg.update(b'GeeksForGeeks')

print(gfg.digest())
