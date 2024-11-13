# At first, we have to import the 'Shelve' module.
import shelve

# In this step, we create a shelf file.
shfile = shelve.open("shelf_file")

# we create a data object which in this case is a book_list.
my_book_list =['bared_to_you', 'The_fault_in_our_stars',
			'The_boy_who_never_let_her_go']

# we are assigning a dictionary key to the list
# which we will want to retrieve
shfile['book_list']= my_book_list

# now, we simply close the shelf file.
shfile.close()
