byte_array = bytearray('XYZ', 'utf-8')

mv = memoryview(byte_array)

print(mv[0])
print(bytes(mv[0:1]))
