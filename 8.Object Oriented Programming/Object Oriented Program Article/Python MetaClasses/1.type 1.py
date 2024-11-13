def init(self, ftype):
	self.ftype = ftype

def getFtype(self):
	return self.ftype

FoodType = type('FoodType', (object, ), {
	'__init__': init,
	'getFtype' : getFtype,
	})

fType = FoodType(ftype ='Vegetarian')
print(fType.getFtype())
