# import zlib and compress
import zlib
s = b'GeeksForGeeks@12345678'
print(len(s))

# using zlib.compress(s) method
t = zlib.compress(s)
print(len(t))
