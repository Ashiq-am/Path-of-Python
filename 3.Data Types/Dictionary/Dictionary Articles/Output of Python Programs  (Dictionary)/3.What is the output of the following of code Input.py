a = {}
b = a.fromkeys([1, False, 3], 'True')
print (all(a))
print (all(b))
