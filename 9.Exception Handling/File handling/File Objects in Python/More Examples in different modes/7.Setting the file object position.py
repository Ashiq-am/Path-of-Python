# Setting the file object position
f = open(__file__, 'r')
lines = f.read(10)
print(lines)

#seek()
print(f.seek(2,2))
lines = f.read(10)
print(lines)
f.close()
