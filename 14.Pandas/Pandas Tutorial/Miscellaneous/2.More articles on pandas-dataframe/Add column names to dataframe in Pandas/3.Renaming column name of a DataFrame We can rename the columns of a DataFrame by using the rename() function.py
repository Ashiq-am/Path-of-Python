# reanming the DataFrame columns
team.rename(columns = {'Code':'Code-Name',
					'Weight':'Weight in kgs'},
			inplace = True)

# displaying the DataFrame
print(team)
