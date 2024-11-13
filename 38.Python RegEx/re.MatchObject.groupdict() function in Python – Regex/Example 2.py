import re

"""We create a re.MatchObject and store it in 
match_object variable 
the '()' parenthesis are used to define a 
specific group"""

match_object = re.match(
	r'(?P<Username>\w+)@(?P<Website>\w+)\.(?P<Domain>\w+)', '1234567890')

""" w in above pattern stands for alphabetical character 
	+ is used to match a consecutive set of characters 
	satisfying a given condition 
	so w+ will match a consecutive set of alphabetical characters 
	The ?P<Username> in '()'(the round brackets) is 
	used to capture subgroups of strings satisfying 
	the above condition and the groupname is 
	specified in the ''(angle brackets)in this 
	case its Username."""

# Following line will raise AttributeError exception
print(match_object.groupdict())
