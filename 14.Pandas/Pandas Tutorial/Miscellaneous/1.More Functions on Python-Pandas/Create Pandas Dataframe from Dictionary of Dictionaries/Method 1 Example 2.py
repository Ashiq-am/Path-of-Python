# import pandas module
import pandas

# create student dictionary of dictionaries with
# 5 students with Age ,subject and address
data = {'Ojaswi': {'Age': 15, 'subject': 'java', 'Address': 'Hyderabad'},
		'Rohith': {'Age': 9, 'subject': 'python', 'Address': 'Hyderabad'},
		'Gnanesh': {'Age': 15, 'subject': 'c/c++', 'Address': 'Guntur'},
		'divya': {'Age': 21, 'subject': 'html', 'Address': 'ponnur'},
		'ramya': {'Age': 15, 'subject': 'c/c++', 'Address': 'delhi'}}

# create pandas dataframe from dictionary of
# dictionaries
data = pandas.DataFrame(data)

# display
data
