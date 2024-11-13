import struct

# Format: h is short in C type
# Format: l is long in C type
# Format 'hhl' stands for 'short short long'
var = struct.pack('hhl',1,2,3)
print(var)

# Format: i is int in C type
# Format 'iii' stands for 'int int int'
var = struct.pack('iii',1,2,3)
print(var)
