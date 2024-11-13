@functools.wraps(org_init)
def new_init(self, *args, **kwargs):

	# calls the init method of class
	org_init(self, *args, **kwargs)

	# add an extra attribute and store
	# creation time
	self._created = time.time()

# reference of new_init is assigned to
# __init__ method and executes when
# callable creates the class object.
cl.__init__ = new_init
