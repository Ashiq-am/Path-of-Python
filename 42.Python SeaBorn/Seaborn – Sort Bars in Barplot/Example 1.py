# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Initialize data
State = ["Rajasthan", "Bihar", "Madhya Pradesh",
		"Gujarat", "Maharashtra"]
growth = [342239, 94163, 308245, 196024, 307713]


# Create a pandas dataframe
df = pd.DataFrame({"State": State,
				"Growth": growth})


# sort dataframe
df.sort_values('Growth')


# make barplot and sort bars
sns.barplot(x='State',
			y="Growth", data=df,
			order=df.sort_values('Growth').State)
