import time
class ObjectCreationTime(object):
	def __init__(self, objName):
		self._created = time.time()
		self._objName = objName

	def __lt__(self, other):
		print('Creation Time:\n'
			'% s:% f\n % s:% f' %(self._objName, self._created,
								other._objName, other._created))
		return self._created < other._created

	def __gt__(self, other):
		print('Creation Time:\n'
			'% s:% f\n % s:% f' %(self._objName, self._created,
								other._objName, other._created))
		return self._created > other._created

obj1 = ObjectCreationTime('obj1')
obj2 = ObjectCreationTime('obj2')
print(obj1 < obj2)
print(obj1 > obj2)
