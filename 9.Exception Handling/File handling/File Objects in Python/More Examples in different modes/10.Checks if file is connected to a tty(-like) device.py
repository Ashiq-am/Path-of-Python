# Checks if file is connected to a tty(-like) device
f = open(__file__, 'r')

#isatty()
print(f.isatty())
f.close()
