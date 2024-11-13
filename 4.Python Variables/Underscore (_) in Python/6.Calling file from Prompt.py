''



'''

>>> from class_file import *
>>> public_api() 
public api 

>>> _private_api() 
Traceback (most recent call last): 
File "<stdin>", line 1, in <module> 
NameError: name '_private_api' is not defined 

>>> import class_file 
>>> class_file.public_api() 
public api 
>>> class_file._private_api() 
private api 


'''