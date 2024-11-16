import pandas as pd


data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
		{'area': 'cape-town', 'rainfall': 70, 'temperature': 25},
		{'area': 'mumbai', 'rainfall': 200, 'temperature': 39 }]

df = pd.DataFrame.from_dict(data)

df
