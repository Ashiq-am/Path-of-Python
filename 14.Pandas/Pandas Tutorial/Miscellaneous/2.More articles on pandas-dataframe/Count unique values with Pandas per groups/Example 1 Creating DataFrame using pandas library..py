# importing library
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

# creating DataFrame for the data using
# pandas DataFrame function.
car_df = pd.DataFrame(car_data)

# printng the dataframe
car_df
