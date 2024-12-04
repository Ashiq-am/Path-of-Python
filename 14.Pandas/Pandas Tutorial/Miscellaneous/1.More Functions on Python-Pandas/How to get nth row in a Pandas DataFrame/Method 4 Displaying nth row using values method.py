import pandas as pd
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Price': [1200, 800, 400, 200, 250],
    'Stock': [15, 30, 20, 50, 25]
}

df=pd.DataFrame(data)
nth_row = df.values[2]
print(nth_row)