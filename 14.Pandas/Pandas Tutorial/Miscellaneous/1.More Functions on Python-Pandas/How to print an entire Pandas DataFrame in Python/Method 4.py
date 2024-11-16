import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data,
				columns=data.feature_names)

# Converts the dataframe into str object with fromatting
print(df.to_markdown())
