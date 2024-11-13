# import zlib and crc32
import zlib

s = b'I love python, Hello world'
# using zlib.crc32() method
t = zlib.crc32(s)

print(t)
