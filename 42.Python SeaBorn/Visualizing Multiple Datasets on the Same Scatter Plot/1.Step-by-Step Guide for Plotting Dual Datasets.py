import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating sample data
data1 = pd.DataFrame({
    'x': range(10),
    'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'label': 'Dataset 1'
})

data2 = pd.DataFrame({
    'x': range(10),
    'y': [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
    'label': 'Dataset 2'
})
