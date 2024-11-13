from collections import OrderedDict
seq = ('name', 'age', 'gender')
dict = OrderedDict.fromkeys(seq)

# Output = {'age': None, 'name': None, 'gender': None}
print (str(dict))
dict = OrderedDict.fromkeys(seq, 10)

# Output = {'age': 10, 'name': 10, 'gender': 10}
print (str(dict))
