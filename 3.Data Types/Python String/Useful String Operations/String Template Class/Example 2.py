# A Python program to demonstrate the
# working of the string template
from string import Template

# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
	print (t.substitute(name = i[0], marks = i[1]))
