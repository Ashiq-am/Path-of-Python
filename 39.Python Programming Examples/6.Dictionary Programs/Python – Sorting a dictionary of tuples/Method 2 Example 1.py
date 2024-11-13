# import oOrderedDict module
from collections import OrderedDict

# declare a dictionary of tuple with student data
data = {'student3': ('bhanu', 10), 'student2': ('uma', 12),
		'student4': ('sai', 11), 'student1': ('suma', 11)}

# sort student dictionary of tuple based
# on values using OrderedDict
print(OrderedDict(sorted(data.values())))
print()

# sort student dictionary of tuple based
# on items using OrderedDict
print(OrderedDict(sorted(data.items())))
