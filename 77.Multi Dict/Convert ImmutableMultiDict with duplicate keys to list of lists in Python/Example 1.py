# Importing library
from werkzeug.datastructures import ImmutableMultiDict

d = ImmutableMultiDict([('Subject', 'Chemistry'),
						('Period', '1st'),
						('Period', '4th')])
print(list(d.lists()))
