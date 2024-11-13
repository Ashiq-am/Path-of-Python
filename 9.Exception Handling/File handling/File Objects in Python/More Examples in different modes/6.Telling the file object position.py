# Telling the file object position
f = open(__file__, 'r')
lines = f.read(10)

#tell()
print(f.tell())
f.close()
