# import pandas
import pandas as pd

df = pd.DataFrame({"A": [3, 4, 5],
				"B": ['c', 'd', 'e']},
				index =['I', 'II', 'III'])

# Using pandas.to_markdown() method
gfg = df.to_markdown()

print(gfg)
