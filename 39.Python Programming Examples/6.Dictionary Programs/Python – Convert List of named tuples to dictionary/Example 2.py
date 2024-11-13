# import named tuple
from collections import namedtuple

# create a nmaed tuple named DETAILS with one column
DETAILS = namedtuple("DETAILS", "Name")

# create 5 students
a = [DETAILS("ojaswi"),
	DETAILS("sireesha"),
	DETAILS("gnanesh"),
	DETAILS("priyank"),
	DETAILS("ojaswi")]

# convert into dictionary
# using dict method
for i in a:
	print(dict(i._asdict()))
