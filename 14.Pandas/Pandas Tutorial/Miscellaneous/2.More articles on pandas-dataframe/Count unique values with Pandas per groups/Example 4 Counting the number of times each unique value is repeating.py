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

            'Gear': [3, 3, 4, 4, 5, 4, 3,
                     3, 3, 3, 3, 3, 4, 4, 4],

            'Cylinder': [6, 8, 4, 4, 6, 6, 8,
                         8, 8, 8, 8, 8, 4, 4, 4]}

# creating DataFrame for the data using pandas
car_df = pd.DataFrame(car_data)

# counting number of times each unique values
# present in the perticular group using
# value_counts() function
gear_count = pd.value_counts(car_df.Gear)
cyl_count = pd.value_counts(car_df.Cylinder)

# another way of obtaining the same output
g_count = car_df['Gear'].value_counts()
cy_count = car_df['Cylinder'].value_counts()
print('----Output from first method-----')

# printing number of times each unique
# values present in the perticular group
print(gear_count)
print(cyl_count)

# printing output from the second method
print('----Output from second method----')
print(g_count)
print(cy_count)
