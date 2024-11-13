# In this example we will see
# the different types of objects
# of sub class of shelve class
import shelve

# importing bsddb module to create
# a bsddb object which can support
# metioned next(), first() methods..
import bsddb

# Shelve Class :
d = {1 : 'geeks', 2 : 'GfG'}

# Dictionary object as parameter
Shelf_obj = shelve.Shelf(d)

print(type(Shelf_obj))

# BsdDbShelf Class :
bsddb_file = bsddb.btopen('spam.db', 'c')

# bsddb object as parameter
bsddb_obj = shelve.BsdDbShelf(bsddb_file)

print(type(bsddb_obj))

# DbfilenameShelf Class :
# File name as parameter
Dbfile_obj = shelve.open('file_name', writeback = True)

print(type(Dbfile_obj))
