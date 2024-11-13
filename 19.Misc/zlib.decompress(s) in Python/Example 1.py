# import zlib and decompress
import zlib


s = b'This is GFG author, and final year student.'

# using zlib.compress(s) method
t = zlib.compress(s)
print("Compressed String")
print(t)

print("\nDecompressed String")
print(zlib.decompress(t))
