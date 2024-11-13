# defining a SuperClass
class SuperClass:
	def __init_subclass__(cls, default_name, **kwargs):
		cls.default_name = default_name

# defining a subclass
class SubClass1(SuperClass, default_name ="SubClass1"):
	pass

# defining another subclass
class SubClass2(SuperClass, default_name ="SubClass2"):
	default_name = "InheritedClass"


# references for subclasses
subClass1 = SubClass1()
subClass2 = SubClass2()

print(subClass1.default_name)
print(subClass2.default_name)
