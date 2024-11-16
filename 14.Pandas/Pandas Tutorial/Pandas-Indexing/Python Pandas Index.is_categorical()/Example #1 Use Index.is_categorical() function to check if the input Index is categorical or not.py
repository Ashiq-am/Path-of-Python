# importing pandas as pd
import pandas as pd

# Creating the categorical Index
idx = pd.Index(['Labrador', 'Beagle', 'Mastiff', 'Lhasa',
					'Husky', 'Beagle']).astype('category')

# Print the Index
idx
