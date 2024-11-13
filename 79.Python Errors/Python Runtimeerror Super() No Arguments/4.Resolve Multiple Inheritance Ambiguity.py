class ParentA:
	def show(self):
		print("Method in ParentA")

class ParentB:
	def show(self):
		print("Method in ParentB")

class Child(ParentA, ParentB):
	def show(self):
		super(Child, self).show()
		print("Method in Child")


child_instance = Child()


child_instance.show()
