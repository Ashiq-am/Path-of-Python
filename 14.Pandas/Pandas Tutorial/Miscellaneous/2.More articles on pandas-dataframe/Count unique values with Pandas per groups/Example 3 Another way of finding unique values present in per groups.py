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

            'Cylinder': [6, 8, 4, 4, 6, 6, 8, 8,
                         8, 8, 8, 8, 4, 4, 4]}

# creating DataFrame for the data using pandas
car_df = pd.DataFrame(car_data)

# finding unique values present in the
# groups using unique() function
unique_gear = pd.unique(car_df.Gear)
unique_cyl = pd.unique(car_df.Cylinder)

# printing the unique values present in the Gear column
print(f"Unique values present in Gear column are: {unique_gear}")

# printing the unique values present in the Cylinder column
print(f"Unique values present in Cylinder column are: {unique_cyl}")
