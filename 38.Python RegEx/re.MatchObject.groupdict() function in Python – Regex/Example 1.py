import re

"""We create a re.MatchObject and store it in 
match_object variable 
the '()' parenthesis are used to define a 
specific group"""

match_object = re.match(
	r'(?P<Username>\w+)@(?P<Website>\w+)\.(?P<Domain>\w+)', 'jon@geekforgeeks.org')

""" w in above pattern stands for alphabetical character 
	+ is used to match a consecutive set of characters 
	satisfying a given condition 
	so w+ will match a consecutive set of alphabetical characters 
	The ?P<Username> in '()'(the round brackets) is 
	used to capture subgroups of strings satisfying 
	the above condition and the groupname is 
	specified in the ''(angle brackets)in this 
	case its Username."""

# generating a dictionary from the given emailID
details = match_object.groupdict()

# printing the dictionary
print(details)
