# import zlib and crc32
import zlib

s = b'Hello GeeksForGeeks'
# using zlib.crc32() method
t = zlib.crc32(s)

print(t)
