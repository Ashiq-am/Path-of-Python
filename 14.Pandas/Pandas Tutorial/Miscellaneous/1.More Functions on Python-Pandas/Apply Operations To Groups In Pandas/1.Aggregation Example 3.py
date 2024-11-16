# Import required libraries
import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame({"dept": np.random.choice(["IT", "HR", "Sales", "Production"], size=50),
				"gender": np.random.choice(["F", "M"], size=50),
				"age": np.random.randint(22, 60, size=50),
				"salary": np.random.randint(20000, 90000, size=50)})
df.index.name = "emp_id"

# Calculate mean salaries and min-max age of employees
# in different departments for gender groups
df.groupby(['dept', 'gender']).agg({'salary': 'mean', 'age': ['min', 'max']})
