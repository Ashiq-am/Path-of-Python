# help function
def help():
	sa = """Usage :- 
$ ./todo add "todo item" # Add a new todo 
$ ./todo ls			 # Show remaining todos 
$ ./todo del NUMBER	 # Delete a todo 
$ ./todo done NUMBER	 # Complete a todo 
$ ./todo help			 # Show usage 
$ ./todo report		 # Statistics"""
	sys.stdout.buffer.write(sa.encode('utf8'))
