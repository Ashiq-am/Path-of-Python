# open both files
with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # write content to second file
        secondfile.write(line)
