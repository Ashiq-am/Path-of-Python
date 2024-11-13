def init(self, ftype):
	self.ftype = ftype

def getFtype(self):
	return self.ftype

FoodType = type('FoodType', (object, ), {
	'__init__': init,
	'getFtype' : getFtype,
	})

def vegFoods(self):
	return {'Spinach', 'Bitter Guard'}

## creating subclass using type
VegType = type('VegType', (FoodType, ), {
	'vegFoods' : vegFoods,
	})


vType = VegType(ftype ='Vegetarian')
print(vType.getFtype())
print(vType.vegFoods())
