# import module
import pandas as pd

# List
Person = [ ['Satyam', 21, 'Patna' , 'India' ],
			['Anurag', 23, 'Delhi' , 'India' ],
			['Shubham', 27, 'Coimbatore' , 'India' ],
			["Saurabh", 23, "Delhi", "india"]]

#Create a DataFrame object
df = pd.DataFrame(Person,
				columns = ['Name' , 'Age', 'City' , 'Country'])

# new list to append into df
list = ['Ujjawal', 22, 'Fathua', 'India']

# usinf iloc
df.iloc[2] = list

# display
display(df)
