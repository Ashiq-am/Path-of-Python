# importing pandas as pd
import pandas as pd

# Create the MultiIndex
midx = pd.MultiIndex.from_tuples([(10, 'Ten'), (10, 'Twenty'),
								(20, 'Ten'), (20, 'Twenty')],
									names =['Num', 'Char'])

# Print the MultiIndex
print(midx)
