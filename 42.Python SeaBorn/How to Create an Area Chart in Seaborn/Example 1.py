import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set seaborn style
sns.set_theme()

#define DataFrame
data = {'period': [1, 2],
				'rohit': [10, 5],
				'vikey': [5, 19],
				}

df = pd.DataFrame(data)

#create area chart
plt.stackplot(df.period, df.rohit, df.vikey,
			labels=['rohit', 'vikey'])
