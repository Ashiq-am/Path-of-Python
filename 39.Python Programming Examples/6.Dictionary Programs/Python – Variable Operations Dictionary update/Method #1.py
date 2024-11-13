# Python3 code to demonstrate working of
# Variable Operations Dictionary update
# Using lambda + dictionary comprehension

# helpr functions
hlper_fnc = {'Gfg': lambda: x + y,
		'best': lambda: x * y}

# initializing variables
x = 6
y = 7

# Variable Operations Dictionary update
# Using lambda + dictionary comprehension
res = {key: val() for key, val in hlper_fnc.items()}

# printing result
print("The Initialized dictionary : " + str(res))
