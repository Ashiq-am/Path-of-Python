# Create a dictionary with student details
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind',
							'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
				'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics',
							'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths',
														'Physics', 'Chemistry'],
				'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
			}

# Convert dictionary to a DataFrame
df = pd.DataFrame(student_details)
print(df)
