city: str = field(init=False, default="patna", repr=True, hash=False)

# object of the class
emp = employee("Satyam", "ksatyam858", 21)
hash(emp)
