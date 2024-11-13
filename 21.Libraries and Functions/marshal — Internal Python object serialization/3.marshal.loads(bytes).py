# Python code to demonstrate de-serialization
import marshal

data = {12:'twelve', 'feep':list('ciao'), 1.23:4+5j,
		(1,2,3):u'wer'}
bytes = marshal.dumps(data)
redata = marshal.loads(bytes)

print (redata)
