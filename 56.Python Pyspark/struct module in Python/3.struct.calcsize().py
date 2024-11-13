import struct
var = struct.pack('?hil', True, 2, 5, 445)
print(var)
# Returns the size of the structure
print(struct.calcsize('?hil'))
print(struct.calcsize('qf'))
