import pandas as pd
import numpy as np

# Creating a DataFrame with random numerical and string columns
np.random.seed(42) # Setting seed for reproducibility

data = {
	'Numeric_Column': np.random.randint(1, 100, 4),
	'String_Column': np.random.choice(['A', 'B', 'C', 'D'], 4)
}

df = pd.DataFrame(data)
df.info()
