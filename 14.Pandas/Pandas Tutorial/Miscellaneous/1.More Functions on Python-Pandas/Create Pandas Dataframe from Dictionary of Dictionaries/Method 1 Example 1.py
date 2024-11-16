# import pandas module
import pandas

# create student dictionary of dictionaries
# with 3 students with Age and address
data = {'Ojaswi': {'Age': 15, 'Address': 'Hyderabad'},
		'Rohith': {'Age': 9, 'Address': 'Hyderabad'},
		'Gnanesh': {'Age': 15, 'Address': 'Guntur'}}

# create pandas dataframe from dictionary of
# dictionaries
data = pandas.DataFrame(data)

# display
print(data)
