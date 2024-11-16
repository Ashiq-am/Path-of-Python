# importing pandas as pd
import pandas as pd

# Create the MultiIndex
midx = pd.MultiIndex.from_arrays([['Beagle', 'Sephard', 'Labrador', 'Retriever'],
									[8, 4, 11, 3], ['A1', 'B1', 'A2', 'C1']])

# Print the MultiIndex
print(midx)
