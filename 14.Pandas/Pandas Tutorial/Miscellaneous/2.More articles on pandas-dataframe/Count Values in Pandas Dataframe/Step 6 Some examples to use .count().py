# count of student with grater
# than 11 marks in physics
print("Count of students with physics marks greater than 11 is->",
	dataframe[dataframe['Physics'] > 11]['Name'].count())

# resultant of above dataframe
dataframe[dataframe['Physics']>11]
