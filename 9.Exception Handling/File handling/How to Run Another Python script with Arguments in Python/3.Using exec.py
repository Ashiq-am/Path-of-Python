# Define arguments
arg1 = "Geeks"
arg2 = "for"
arg3 = "Geeks"

# Execute called script with the arguments
exec(open("called_script.py").read(), {
	'arg1': arg1, 'arg2': arg2, 'arg3': arg3})
