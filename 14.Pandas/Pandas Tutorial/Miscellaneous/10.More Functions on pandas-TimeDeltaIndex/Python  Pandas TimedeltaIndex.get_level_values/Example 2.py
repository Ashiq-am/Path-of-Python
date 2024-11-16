# importing pandas as pd
import pandas as pd

# Create the MultiIndex object
midx = pd.MultiIndex.from_arrays((['AB', 'BC', 'CD', 'DE'],
								['EF', 'FG', 'GH', 'HI']))

# Print the MultiIndex object
print(midx)
