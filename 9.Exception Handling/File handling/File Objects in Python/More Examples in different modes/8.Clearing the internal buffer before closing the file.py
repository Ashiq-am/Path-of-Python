# Clearing the internal buffer before closing the file
f = open(__file__, 'r')
lines = f.read(10)

#flush()
f.flush()
print(f.read())
f.close()
