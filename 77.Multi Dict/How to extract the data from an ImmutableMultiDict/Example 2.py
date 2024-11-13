from werkzeug.datastructures import ImmutableMultiDict

data = ImmutableMultiDict([('username', 'Ryan'),
						('password', 'QWERTY'),
						('password',123456)])
print(data.getlist('password'))
