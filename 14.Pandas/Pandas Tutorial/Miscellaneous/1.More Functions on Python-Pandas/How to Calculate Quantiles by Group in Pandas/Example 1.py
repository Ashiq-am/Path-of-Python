# Importing libraries
import pandas as pd

# Storing data in dictionary
game = {'Player': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
						'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
						'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
		'wins': [2, 4, 4, 5, 6, 9, 13, 13, 15, 15, 14, 13,
				11, 9, 9, 8, 8, 16, 19, 21, 14, 20, 19, 18]
		}
# Creating data frame
df = pd.DataFrame(game)

# calculating quantile
df.groupby('Player').quantile(0.5)
