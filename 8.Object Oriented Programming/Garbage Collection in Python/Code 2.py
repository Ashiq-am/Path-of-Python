def create_cycle():

	# create a list x
	x = [ ]

	# A reference cycle is created
	# here as x contains reference to
	# to self.
	x.append(x)

create_cycle()
