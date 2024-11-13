# Python program to demonstrate
# saving a text file


with open('read.txt', 'w') as file:
    books = ['Welcome\n',
             'Geeks\n',
             'to\n',
             'Geeks\n',
             'for\n',
             'Geeks\n',
             'world\n']

    file.writelines("% s\n" % data for data in books)
