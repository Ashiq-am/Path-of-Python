import struct

# '?' -> _BOOL , 'h' -> short, 'i' -> int and 'l' -> long
var = struct.pack('?hil', True, 2, 5, 445)
print(var)

# struct.unpack() return a tuples
# Variables V1, V2, V3,.. are returned as elements of tuple
tup = struct.unpack('?hil', var)
print(tup)

# q -> long long int and f -> float
var = struct.pack('qf', 5, 2.3)
print(var)
tup = struct.unpack('qf', var)
print(tup)
