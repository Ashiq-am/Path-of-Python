# Writing a file
f = open(__file__, 'a+')
lines = f.readlines()

#writelines()
f.writelines(lines)
f.close()
