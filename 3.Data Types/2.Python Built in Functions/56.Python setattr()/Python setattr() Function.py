class Person:
	def __init__(self):
		pass

p = Person()
setattr(p, 'name', 'kiran')
print(f"name: {p.name}")
