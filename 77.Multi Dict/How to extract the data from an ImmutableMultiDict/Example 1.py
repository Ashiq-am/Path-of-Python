from werkzeug.datastructures import ImmutableMultiDict

data = ImmutableMultiDict([('username', 'Ryan'),
						('password', 'QWERTY')])
print(data.get('username'))
