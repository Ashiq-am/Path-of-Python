# Python script to demonstrate namedtuple()

# importing nametuple() from collections module
from collections import namedtuple

# Declaring namedtuple()
Contributor = namedtuple('Contributor', ['topic', 'author', 'post'])

# Adding values
C = Contributor('Difference between DataClass vs NamedTuple vs Object in Python',
                'night_fury1',
                'Technical Content Writer Intern')

# Access using index
print("The Article Topic : ", end="")
print(C[0])

# Access using name
print("The Article Contributor Name : ", end="")
print(C.author)

# Access using getattr()
print("The Article Contributor Post : ", end="")
print(getattr(C, 'post'))
