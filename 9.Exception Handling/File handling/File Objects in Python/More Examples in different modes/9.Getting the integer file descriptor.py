# Getting the integer file descriptor
f = open(__file__, 'r')

#fileno()
print(f.fileno())
f.close()
