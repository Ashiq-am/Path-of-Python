# Reading a file
f = open(__file__, 'r')

#readline()
text = f.readlines(25)
print(text)
f.close()
