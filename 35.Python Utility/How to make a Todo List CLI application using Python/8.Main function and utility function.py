# code
def nec():
    # utility function used in done and report function
    try:
        f = open('todo.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c + 1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))

    # Main program


if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv

        if (args[1] == 'del'):
            args[1] = 'deL'

        if (args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing todo string. Nothing added!".encode('utf8'))

        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking todo as done.".encode('utf8'))

        elif (args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting todo.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])

    except Exception as e:

        s = """Usage :- 
$ ./todo add "todo item" # Add a new todo 
$ ./todo ls			 # Show remaining todos 
$ ./todo del NUMBER	 # Delete a todo 
$ ./todo done NUMBER	 # Complete a todo 
$ ./todo help			 # Show usage 
$ ./todo report		 # Statistics"""
        sys.stdout.buffer.write(s.encode('utf8'))
