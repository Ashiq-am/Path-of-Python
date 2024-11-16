import pandas as pd

# List of dictionaries containing data
data = [
	{"Name": "John Smith", "Age": 35, "Address": "123 Main St, New York, NY 10001"},
	{"Name": "Jane Doe", "Age": 28, "Address": "456 Park Ave, Newark, NJ 70004"},
	{"Name": "Joe Schmo", "Age": 55, "Address": "789 Broad Way, Jersey City, NJ 07306"},
	{"Name": "Sally Smith", "Age": 42, "Address": "321 Maple St, Hoboken, NJ 07030"},
	{"Name": "Bob Johnson", "Age": 28, "Address": "654 Cedar Blvd, Union City, NJ 07087"},
	{"Name": "Sue Johnson", "Age": 29, "Address": "912 Oak St, Weehawken, NJ 07086"},
	{"Name": "Bill Williams", "Age": 33, "Address": "245 Pine Rd, West New York, NJ 07093"},
	{"Name": "Mary Johnson", "Age": 25, "Address": "369 Birch Ave, Guttenberg, NJ 07093"},
	{"Name": "Tom Williams", "Age": 44, "Address": "159 Willow St, Hoboken, NJ 07030"},
]

# Create the DataFrame
df = pd.DataFrame(data)

# Filter the DataFrame to only include the mentioned columns
df = df.filter(like="Address")

print(df)
