
try:

    trying_to_check_error

except NameError as err:
    print(err, 'Error Caused') # Would not work in Python 3.x



''' 

Output in Python 2.x: 

name 'trying_to_check_error' is not defined Error Caused 



Output in Python 3.x : 

File "a.py", line 3 

	except NameError, err: 

					^ 

SyntaxError: invalid syntax 

'''
