# create a list of names
names = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']

# create a list of subjects
subjects = ['java', 'python', 'R', 'cpp', 'bigdata']

# create a list of marks
marks = [78, 100, 97, 89, 80]

# use enumerate() and zip() function
# to iterate the lists
for i, (names, subjects, marks) in enumerate(zip(names, subjects, marks)):
	print(i, names, subjects, marks)
