# At first, we import the 'Shelve' module.
import shelve

# In this step, we create a shelf file.
var = shelve.open("shelf_file")

# Now, this 'var' variable points to all the
# data objects in the file 'shelf_file'.
print(var['book_list'])

# now, we simply close the file 'shelf_file'.
var.close()
