# import DataFrame
import pandas as pd

# using DataFrame.to_html() method
gfg = pd.DataFrame({'Name': ['Marks'],
					'Jitender': ['78'],
					'Rahul': ['77.9']})

print(gfg.to_html())
