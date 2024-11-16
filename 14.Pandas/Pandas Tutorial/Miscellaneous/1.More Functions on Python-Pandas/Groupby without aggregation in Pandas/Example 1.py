# importing python libraries and breast_cancer dataset from sklearn
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_breast_cancer

# data is loaded in a DataFrame
cancer_data = load_breast_cancer()
df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
df['target'] = pd.Series(cancer_data.target)
df.head()
