# importing libraries
import pandas as pd

# storing the data of cars in the dictionary
car_data = {'Model Name': ['Valiant',
                           'Duster 360',
                           'Merc 240D',
                           'Merc 230',
                           'Merc 280',
                           'Merc 280C',
                           'Merc 450SE',
                           'Merc 450SL',
                           'Merc 450SLC',
                           'Cadillac Fleetwood',
                           'Lincoln Continental',
                           'Chrysler Imperial',
                           'Fiat 128',
                           'Honda Civic',
                           'Toyota Corolla'],

            'Gear': [3, 3, 4, 4, 5, 4, 3, 3,
                     3, 3, 3, 3, 4, 4, 4],

            'Cylinder': [6, 8, 4, 4, 6, 6, 8,
                         8, 8, 8, 8, 8, 4, 4, 4]}

# creating DataFrame for the data using pandas
car_df = pd.DataFrame(car_data)

# finding unique values present in the perticular group.
name_count = pd.unique(car_df['Model Name'])
gear_count = pd.unique(car_df.Gear)
cyl_count = pd.unique(car_df.Cylinder)

# initializing variable to 0 for counting
name_unique = 0
gear_unique = 0
cyl_unique = 0

# writing separate for loop of each groups
for item in name_count:
    name_unique += 1

for item in gear_count:
    gear_unique += 1

for item in gear_count:
    cyl_unique += 1

# printing the number of unique values present in each group
print(f'Number of unique values present in Model Name: {name_unique}')
print(f'Number of unique values present in Gear: {gear_unique}')
print(f'Number of unique values present in Cylinder: {cyl_unique}')
