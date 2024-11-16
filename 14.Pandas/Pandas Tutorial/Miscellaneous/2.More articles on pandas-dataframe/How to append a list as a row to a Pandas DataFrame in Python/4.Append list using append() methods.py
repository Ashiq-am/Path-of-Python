# import module
import pandas as pd

# List
Person = [ ['Satyam', 21, 'Patna' , 'India' ],
			['Anurag', 23, 'Delhi' , 'India' ],
			['Shubham', 27, 'Coimbatore' , 'India' ]]

#Create a DataFrame object
df = pd.DataFrame(Person,
				columns = ['Name' , 'Age', 'City' , 'Country'])

# new list to append into df
list = [["Manjeet", 25, "Delhi", "india"]]

# using append
df = df.append(pd.DataFrame( list,
			columns=[ 'Name', 'Age', 'City', 'Country']),
			ignore_index = True)

# display df
display(df)
