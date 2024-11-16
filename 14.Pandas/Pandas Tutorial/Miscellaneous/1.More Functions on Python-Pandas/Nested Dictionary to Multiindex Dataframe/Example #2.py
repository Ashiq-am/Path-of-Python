# Import module
import pandas as pd

# Nested dictionary to convert it into multiindex dataframe
nested_dict = {'India': {'State': ['Maharashtra', 'West Bengal',
								'Uttar Pradesh', 'Bihar', 'Karnataka'],
						'Capital': ['Mumbai', 'Kolkata', 'Lucknow',
									'Patna', 'Bengaluru']},

			'America': {'State': ['California', 'Florida', 'Georgia',
									'Massachusetts', 'New York'],
						'Capital': ['Sacramento', 'Tallahassee', 'Atlanta',
									'Boston', 'Albany']}}

reformed_dict = {}
for outerKey, innerDict in nested_dict.items():
	for innerKey, values in innerDict.items():
		reformed_dict[(outerKey, innerKey)] = values

# Display multiindex dataframe
multiIndex_df = pd.DataFrame(reformed_dict)
multiIndex_df
