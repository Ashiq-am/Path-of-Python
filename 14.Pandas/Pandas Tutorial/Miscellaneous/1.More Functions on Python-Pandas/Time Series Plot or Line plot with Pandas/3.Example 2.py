import pandas as pd

# Create a list of data to
# be represented in x-axis
subjects = [ 'Math' , 'English' , 'History' ,
			'Chem' , 'Geo' , 'Physics' , 'Bio' , 'CS' ]

# Create a list of data to be
# represented in y-axis
stress = [ 9 , 3 , 5 , 1 , 8 , 5 , 10 , 2 ]

# Create second list of data
# to be represented in y-axis
grades = [ 15 , 10 , 7 , 8 , 11 , 8 , 17 , 20 ]

# Create a dataframe using the three lists
df = pd.DataFrame(list(zip( stress , grades )),
				index = subjects ,
				columns = [ 'Stress' , 'Grades' ])
df
