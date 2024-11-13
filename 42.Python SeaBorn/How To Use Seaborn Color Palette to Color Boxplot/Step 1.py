# import the required library
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Generate some random data
np.random.seed(45)
df = pd.DataFrame({
	'Corn': np.random.normal(40, 15, 100),
	'Rice': np.random.normal(60, 10,100),
	'Wheat': np.random.normal(80, 5, 100),
	'Peas': np.random.normal(30, 13, 100),
})
print(df)
