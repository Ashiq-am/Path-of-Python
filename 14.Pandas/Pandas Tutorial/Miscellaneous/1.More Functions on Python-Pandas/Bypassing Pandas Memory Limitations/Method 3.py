import pandas as pd

data = pd.read_csv('train_dataset.csv', dtype={'Age': 'int32'})

print(data.info())
