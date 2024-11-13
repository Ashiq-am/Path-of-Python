import typing

class Base:
	@typing.final
	def done(self):
		print("Base")

class Child(Base):
	def done(self): # Error: Method "done" cannot override final method defined in class "Base"
		print("Child")

@typing.final
class Geek:
	pass

class Other(Geek): # Error: Base class "Geek" is marked final and cannot be subclassed
	pass
