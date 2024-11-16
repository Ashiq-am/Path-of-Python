# Import required libraries
import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame({"dept": np.random.choice(["IT", "HR", "Sales", "Production"], size=50),
				"gender": np.random.choice(["F", "M"], size=50),
				"age": np.random.randint(22, 60, size=50),
				"salary": np.random.randint(20000, 90000, size=50)})
df.index.name = "emp_id"

# Calculate min, max, mean and count of salaries
# in different departments for males and females
df.groupby(['dept', 'gender'])['salary'].agg(["min", "max", "mean", "count"])
