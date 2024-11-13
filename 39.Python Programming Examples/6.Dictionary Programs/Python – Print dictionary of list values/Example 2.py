# create a dictionary
# with student names as key
# values as subject details
data = {'manoja': [{'subject1': "java", 'marks': 98},
				{'subject2': "PHP", 'marks': 89}],
		'manoj': [{'subject1': "java", 'marks': 78},
				{'subject2': "PHP", 'marks': 79}],
		'ramya': [{'subject1': "html", 'marks': 78}]}

# get the list of data
# using items() method
for key, values in data.items():
	for i in values:
		print(key, " : ", i)
