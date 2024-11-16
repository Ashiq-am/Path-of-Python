# creating a new pandas
# series object
new_person = pd.Series(['Mansi', 19, True],
					index = ['Name', 'Age',
								'Student'])

# using the .append() function
# to add that row to the dataframe
student_register.append(new_person, ignore_index = True)
