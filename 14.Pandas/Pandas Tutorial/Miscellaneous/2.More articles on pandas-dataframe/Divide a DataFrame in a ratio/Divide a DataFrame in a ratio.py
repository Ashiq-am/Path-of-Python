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
# show the dataframe
df
