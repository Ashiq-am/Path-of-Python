# importing pandas as pd
import pandas as pd

# Creating the first Index
idx1 = pd.Index(['Labrador', 'Beagle', 'Mastiff',
					'Lhasa', 'Husky', 'Beagle'])

# Creating the second Index
idx2 = pd.Index(['Labrador', 'Great_Dane', 'Pug',
		'German_sepherd', 'Husky', 'Pitbull'])

# Print the first and second Index
print(idx1, '\n', idx2)
