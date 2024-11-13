# Reading a line in a file
f = open(__file__, 'r')

#readline()
text = f.readline(20)
print(text)
f.close()
