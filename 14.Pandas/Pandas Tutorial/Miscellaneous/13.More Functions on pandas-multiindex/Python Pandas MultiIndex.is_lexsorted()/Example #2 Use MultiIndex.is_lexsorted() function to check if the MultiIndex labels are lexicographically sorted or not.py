# importing pandas as pd
import pandas as pd

# Create the MultiIndex
midx = pd.MultiIndex.from_arrays([['Anthropology', 'Cryptography',
										'Networking', 'Science'],
											[88, 84, 98, 95]])

# Print the MultiIndex
print(midx)
