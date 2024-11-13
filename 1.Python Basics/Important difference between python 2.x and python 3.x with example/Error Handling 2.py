
try:

    trying_to_check_error

except NameError as err: # 'as' is needed in Python 3.x

    print (err, 'Error Caused')



''' 

Output in Python 2.x: 

(NameError("name 'trying_to_check_error' is not defined",), 'Error Caused') 



Output in Python 3.x : 

name 'trying_to_check_error' is not defined Error Caused 

'''
