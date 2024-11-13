# Python3 code to demonstrate working of
# Variable Operations Dictionary update
# Using lambda + dictionary comprehension
from operator import add, mul

# helpr functions
hlper_fnc = {'Gfg': add,
		'best': mul}

# initializing variables
x = 6
y = 7

# Variable Operations Dictionary update
# Using lambda + dictionary comprehension
res = {'Gfg' : hlper_fnc['Gfg'](x, y), 'best' : hlper_fnc['best'](x, y)}

# printing result
print("The Initialized dictionary : " + str(res))
