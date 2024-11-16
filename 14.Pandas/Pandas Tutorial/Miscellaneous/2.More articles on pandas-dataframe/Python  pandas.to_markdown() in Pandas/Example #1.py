# import pandas
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3],
				"B": [1.1, 2.2, 3.3]},
					index =['a', 'a', 'b'])

# Using pandas.to_markdown() method
gfg = df.to_markdown()

print(gfg)
