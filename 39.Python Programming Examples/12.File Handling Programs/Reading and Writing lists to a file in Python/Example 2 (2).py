# open file form two file objects
f1 = open('gfg.txt', 'r')
f2 = open('gfg.txt', 'r')

# display content of the file
print("\nOutput from readlines():")
print(f1.readlines())

print("\nOutput from read():")
print(f2.read())

# close the files
f1.close()
f2.close()
