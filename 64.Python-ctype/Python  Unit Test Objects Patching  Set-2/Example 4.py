m.upper.return_value = 'HELLO'
print (m.upper('hello'))

assert m.upper.called
m.split.return_value = ['hello', 'world']
print (m.split('hello world'))

m.split.assert_called_with('hello world')
print (m['blah'])

print (m.__getitem__.called)
