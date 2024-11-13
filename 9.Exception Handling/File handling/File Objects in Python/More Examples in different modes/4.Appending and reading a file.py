# Appending and reading a file
f = open(__file__, 'a+')
lines = f.read()
f.write(lines)
f.close()
