import struct
var = struct.pack('bi', 56, 0x12131415)
print(var)
print(struct.calcsize('bi'))
var = struct.pack('ib', 0x12131415, 56)
print(var)
print(struct.calcsize('ib'))
