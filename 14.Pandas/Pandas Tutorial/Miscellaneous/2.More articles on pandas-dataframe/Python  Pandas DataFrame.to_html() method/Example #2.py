# import DataFrame
import pandas as pd

# using DataFrame.to_html() method
gfg = pd.DataFrame({'Name': ['Marks', 'Gender'],
					'Jitender': ['78', 'Male'],
					'Purnima': ['78.9', 'Female']})

print(gfg.to_html())
