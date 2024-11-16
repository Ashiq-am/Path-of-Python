import pandas as pd

data=pd.read_csv('train_dataset.csv')

data = data[['Gender', 'Age', 'openness', 'neuroticism',
			'conscientiousness', 'agreeableness', 'extraversion']]

display(data)
