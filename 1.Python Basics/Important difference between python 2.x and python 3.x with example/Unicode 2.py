"""Python 2.x also supports Unicode"""


print(type('default string '))

print(type(u'string with b '))



''' 

Output in Python 2.x (Unicode and str are different) 

<type 'str'> 

<type 'unicode'> 



Output in Python 3.x (Unicode and str are same) 

<class 'str'> 

<class 'str'> 

'''
