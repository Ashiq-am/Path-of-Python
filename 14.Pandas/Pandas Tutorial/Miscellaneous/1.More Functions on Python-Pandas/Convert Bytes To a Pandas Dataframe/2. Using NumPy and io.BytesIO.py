import numpy as np
import pandas as pd
from io import BytesIO

# Sample bytes data
bytes_data = b'Name,Age,Occupation\nJohn,25,Engineer\nAlice,30,Doctor\nBob,28,Artist'

# Convert bytes to DataFrame using NumPy and io.BytesIO
array_data = np.genfromtxt(
	BytesIO(bytes_data), delimiter=',', names=True, dtype=None, encoding='utf-8')
df_method2 = pd.DataFrame(array_data)

# Display the DataFrame
print(df_method2)
