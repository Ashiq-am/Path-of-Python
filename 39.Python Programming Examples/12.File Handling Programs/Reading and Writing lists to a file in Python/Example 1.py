# assign list
l = ['Geeks', 'for', 'Geeks!']

# open file
with open('gfg.txt', 'w+') as f:
    # write elements of list
    for items in l:
        f.write('%s\n' % items)

    print("File written successfully")

# close the file
f.close()
