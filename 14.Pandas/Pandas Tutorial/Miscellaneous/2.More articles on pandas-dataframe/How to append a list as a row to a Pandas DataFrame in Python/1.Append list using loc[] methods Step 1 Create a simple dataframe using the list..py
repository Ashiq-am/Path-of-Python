import pandas as pd

# List
Person = [ ['Satyam', 21, 'Patna' , 'India' ],
			['Anurag', 23, 'Delhi' , 'India' ],
			['Shubham', 27, 'Coimbatore' , 'India' ]]

#Create a DataFrame object
df = pd.DataFrame(Person,
				columns = ['Name' , 'Age', 'City' , 'Country'])

# display
display(df)
