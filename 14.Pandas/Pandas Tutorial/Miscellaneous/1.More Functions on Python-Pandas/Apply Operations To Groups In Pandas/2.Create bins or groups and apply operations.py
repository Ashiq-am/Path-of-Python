# Import required libraries
import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame({"dept": np.random.choice(["IT", "HR", "Sales", "Production"], size=50),
				"gender": np.random.choice(["F", "M"], size=50),
				"age": np.random.randint(22, 60, size=50),
				"salary": np.random.randint(20000, 90000, size=50)})
df.index.name = "emp_id"

# Create bin intervals
bins = [20, 30, 45, 60]

# Segregate ages into bins of age groups
df['categories'] = pd.cut(df['age'], bins,
						labels=['Young', 'Middle', 'Old'])

# Calculate number of obervations in each age category
df['age'].groupby(df['categories']).count()
