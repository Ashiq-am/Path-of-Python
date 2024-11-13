# import the necessary python packages
import pandas as pd
import numpy as np
import seaborn as sns

# create long-form data
data = pd.DataFrame({'season': np.repeat(['Summer', 'Winter',
										'Spring'], 5),
					'rainfall_amount': [17, 18, 19, 21, 27,
										33, 37, 33, 36, 12,
										14, 15, 16, 21, 22],
					})
# print the data
print(data)

# use seaborn plot and specify the x and y
# columns and specify the dataframe
sns.boxplot(x='season', y='rainfall_amount', data=data)
