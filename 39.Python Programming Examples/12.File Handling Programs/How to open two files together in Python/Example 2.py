# opening file1 in reading mode and file2 in writing mode
with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    # writing the contents of file1 into file2
    f2.write(f1.read())
