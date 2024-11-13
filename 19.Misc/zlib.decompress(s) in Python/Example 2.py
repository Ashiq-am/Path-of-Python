# import zlib and decompress
import zlib


s = b'GeeksForGeeks@12345678'

# using zlib.compress(s) method
t = zlib.compress(s)
print("Compressed String")
print(t)

print("\nDecompressed String")
print(zlib.decompress(t))
