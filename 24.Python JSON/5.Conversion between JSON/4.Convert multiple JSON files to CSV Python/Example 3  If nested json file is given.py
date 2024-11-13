# importing packages
import pandas as pd
import json

# load json file using json.load
with open('file5.json') as file:
	data = json.load(file)

# view data
print(data)

# form the dataframe
df = pd.DataFrame(data['tickets'])

# view dataframe
print(df)

# flattern the dataframe and remove unnecessary columns
for i, item in enumerate(df['Location']):
	df['location_city'] = dict(df['Location'])[i]['City']
	df['location_state'] = dict(df['Location'])[i]['State']

for i, item in enumerate(df['hobbies']):
	df['hobbies_{}'.format(i)] = dict(df['hobbies'])[i]

df = df.drop({'Location', 'hobbies'}, axis=1)

# view dataframe
print(df)

# convert dataframe to csv file
df.to_csv("CSV.csv", index=False)

# load the resultant csv file
result = pd.read_csv("CSV.csv")

# and view the data
print(result)
