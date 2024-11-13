from operator import attrgetter


class geeks:
	def __init__(self, experience, salary):
		self.experience = experience
		self.salary = salary


object1 = geeks(7, 57050)
object2 = geeks(3, 98000)
object5 = geeks(6, 45000)
object4 = geeks(1, 89000)
object3 = geeks(5, 25000)

l = [object4, object3, object5, object2, object1]
max_attr = max(l, key=attrgetter('salary'))
print(max_attr.salary)
