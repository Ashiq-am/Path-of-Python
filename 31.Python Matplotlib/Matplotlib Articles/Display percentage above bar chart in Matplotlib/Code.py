# import modules
import pandas as pd
import matplotlib.pyplot as plt

# assign data
data = pd.DataFrame({'Format': ['Test', 'ODI', 'T20I', 'IPL'],
					'Matches': [90, 350, 98, 204],
					'Runs': [4876, 10773, 1617, 4632]
					})

# dispay data
display(data)
