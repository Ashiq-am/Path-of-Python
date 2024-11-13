# At first, we have to import the 'Shelve' module.
import shelve

# In this step, we create a shelf file.
var = shelve.open("shelf_file", writeback=True)

# inputting total values we want to add
# to the already existing list in shelf_file.
val1 = int(input("Enter the number of values "))

for x in range(val1):
    val = input("\n Enter the value\t")
    var['book_list'].append(val)

    # Now, this 'var' variable will help in printing
    # the data objects in the file 'shelf_file'.
    print(var['book_list'])

    # to make our changes permanent, we use
    # synchronize function.
    var.sync()

    # now, we simply close the file 'shelf_file'.
    var.close()
