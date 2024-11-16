import pandas as pd

# Create a DataFrame with product codes
data = {
    'ProductCode': ['A12345', 'B67890', 'C54321', 'D98765'],
    'Price': [100, 150, 200, 250]
}

df = pd.DataFrame(data)
print(df)
