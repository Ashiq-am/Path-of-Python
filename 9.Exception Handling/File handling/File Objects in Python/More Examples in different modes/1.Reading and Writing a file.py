# Reading and Writing a file
f = open(__file__, 'r+')
lines = f.read()
f.write(lines)
f.close()
