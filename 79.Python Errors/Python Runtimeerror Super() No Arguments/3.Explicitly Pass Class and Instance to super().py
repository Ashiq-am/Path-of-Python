class ParentClass:
	def __init__(self):
		print("ParentClass constructor")

class IntermediateClass(ParentClass):
	def __init__(self):
		super(IntermediateClass, self).__init__()
		print("IntermediateClass constructor")

class ChildClass(IntermediateClass):
	def __init__(self):
		super(ChildClass, self).__init__()
		print("ChildClass constructor")

child_instance = ChildClass()
