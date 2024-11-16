# importing pandas as pd
import pandas as pd

# Creating the Dataframe
df = pd.DataFrame({'num_legs': [4, 4, 2, 2],
				'num_wings': [0, 0, 2, 2],
				'class': ['Mammal', 'Mammal', 'Mammal', 'Bird'],
				'animal': ['Cow', 'Elephant', 'Deer', 'Sparrow'],
				'locomotion': ['Walks', 'Walks', 'Walks', 'Flies']})

# setting the index
df = df.set_index(['class', 'animal', 'locomotion'])

# Print the Dataframe
print(df)
