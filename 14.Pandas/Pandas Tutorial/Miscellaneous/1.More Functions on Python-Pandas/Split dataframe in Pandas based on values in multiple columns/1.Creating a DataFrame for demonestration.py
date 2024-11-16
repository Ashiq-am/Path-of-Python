# importing pandas as pd
import pandas as pd


# dictionary of lists
dict = {'First_Name': ["Aparna", "Pankaj", "Sudhir",
					"Geeku", "Anuj", "Aman",
					"Madhav", "Raj", "Shruti"],
		'Last_Name': ["Pandey", "Gupta", "Mishra",
					"Chopra", "Mishra", "Verma",
					"Sen", "Roy", "Agarwal"],
		'Email_ID': ["apandey@gmail.com", "pankaj@gmail.com",
					"sumishra23@gmail.com", "cgeeku@yahoo.com",
					"anuj24@gmail.com", "amanver@yahoo.com",
					"madhav1998@gmail.com", "rroy7@gmail.com",
					"sagarwal36@gmail.com"],
		'Degree': ["MBA", "BCA", "M.Tech", "MBA", "B.Sc",
				"B.Tech", "B.Tech", "MBA", "M.Tech"],
		'Score': [90, 40, 75, 98, 94, 90, 80, 90, 95]}

# creating dataframe
df = pd.DataFrame(dict)

print(df)
