class Private:
	def __init__(self):
		self.__private_attr = 10

	@property
	def Get_Private_Data(self):
		return self.__private_attr

obj = Private()
print("The Private Data is :", obj.Get_Private_Data)
