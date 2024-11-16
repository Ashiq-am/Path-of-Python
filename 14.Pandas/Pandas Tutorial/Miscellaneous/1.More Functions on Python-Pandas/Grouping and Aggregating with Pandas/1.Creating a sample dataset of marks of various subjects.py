# import module
import pandas as pd

# Creating our dataset
df = pd.DataFrame([[9, 4, 8, 9],
				[8, 10, 7, 6],
				[7, 6, 8, 5]],
				columns=['Maths', 'English',
						'Science', 'History'])

# display dataset
print(df)
