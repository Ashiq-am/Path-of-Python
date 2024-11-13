# import zlib and compress
import zlib
s = b'This is GFG author, and final year student.'
print(len(s))

# using zlib.compress(s) method
t = zlib.compress(s)
print(len(t))
