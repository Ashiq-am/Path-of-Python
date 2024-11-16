import pandas as pd
import numpy as np

Dataset= pd.read_csv("property data.csv")
X = Dataset.iloc[:,0].values

# To calculate mean use imputer class
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X)

X = imputer.transform(X)
print(X)
