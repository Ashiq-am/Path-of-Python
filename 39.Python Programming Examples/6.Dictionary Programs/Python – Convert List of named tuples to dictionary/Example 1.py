# import named tuple
from collections import namedtuple

# create a named tuple named DETAILS with three columns
DETAILS = namedtuple("DETAILS", "Name, Age, Subject")

# create 5 students
a = [DETAILS("ojaswi", 21, "python"),
	DETAILS("sireesha", 21, "python"),
	DETAILS("gnanesh", 23, "php"),
	DETAILS("priyank", 21, "java"),
	DETAILS("ojaswi", 22, "big-data")]

# convert into dictionary
# using dict method
for i in a:
	print(dict(i._asdict()))
