import pandas as pd

# Create a dataframe
from IPython.core.display import display

df = pd.DataFrame({
    'Product_id': ['ABC', 'DEF', 'GHI', 'JKL',
                   'MNO', 'PQR', 'STU', 'VWX'],

    'Stall_no': [37, 38, 9, 50, 7, 23, 33, 4],
    'Grade': [1, 0, 0, 2, 0, 1, 3, 0],

    'Category': ['Fashion', 'Education', 'Technology',
                 'Fashion', 'Education', 'Technology',
                 'Fashion', 'Education'],

    'Demand': [10, 12, 14, 15, 13, 20, 10, 15],
    'charges1': [376, 397, 250, 144, 211, 633, 263, 104],
    'charges2': [11, 12, 9, 13, 4, 6, 13, 15],
    'Max_Price': [4713, 10352, 7309, 20814, 9261,
                  6104, 5257, 5921],

    'Selling_price': [4185.9477, 9271.490256, 6785.701362,
                      13028.91782, 906.553935, 5631.247872,
                      3874.264992, 4820.943]})
display(df)
