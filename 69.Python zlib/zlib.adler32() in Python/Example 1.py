# import zlib and adler32
import zlib

s = b'I love python, Hello world'

# using zlib.adler32() method
t = zlib.adler32(s)

print(t)


