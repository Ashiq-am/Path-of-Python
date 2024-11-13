import struct

# ctypes in imported to create string buffer
import ctypes

# SIZE of the format is calculated using calcsize()
siz = struct.calcsize('hhl')
print(siz)

# Buffer 'buff' is created
buff = ctypes.create_string_buffer(siz)

# struct.pack() returns packed data
# struct.unpack() returns unpacked data
x = struct.pack('hhl', 2, 2, 3)
print(x)
print(struct.unpack('hhl', x))

# struct.pack_into() packs data into buff, doesn't return any value
# struct.unpack_from() unpacks data from buff, returns a tuple of values
struct.pack_into('hhl', buff, 0, 2, 2, 3)
print(struct.unpack_from('hhl', buff, 0))
