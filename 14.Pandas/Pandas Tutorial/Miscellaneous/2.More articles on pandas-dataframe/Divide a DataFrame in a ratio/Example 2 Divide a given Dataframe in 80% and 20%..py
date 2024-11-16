# importing pandas as pd
import pandas as pd

# dictionary
cars = {
'Brand': ['Honda Civic', 'Toyota Corolla',
			'Ford Focus', 'Audi A4', 'Maruti 800',
			'Toyota Innova', 'Tata Safari', 'Maruti Zen',
			'Maruti Omni', 'Honda Jezz'],
'Price': [22000, 25000, 27000, 35000,
			20000, 25000, 31000, 23000,
			26000, 25500]
}

# create the dataframe
df = pd.DataFrame(cars,
				columns = ['Brand',
							'Price'])

# Print the 80% of the dataframe
part_80 = df.sample(frac = 0.8)
print("\n 80% DataFrame:")
print(part_80)

# Print the 20% of the dataframe
part_20 = df.drop(part_80.index)
print("\n 20% DataFrame:")
print(part_20)
