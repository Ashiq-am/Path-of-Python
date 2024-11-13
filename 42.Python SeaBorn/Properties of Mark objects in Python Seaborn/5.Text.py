import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [500, 600, 800, 1000, 1200]}
df = pd.DataFrame(data)

sns.lineplot(x='Year', y='Sales', data=df, color='green')

plt.title('GFG Sales Over Years', fontsize=18, weight='bold', color='blue')
plt.xlabel('Year', fontsize=14, style='italic', color='purple')
plt.ylabel('Sales ($)', fontsize=14, style='italic', color='orange')
plt.xticks(fontsize=12, color='red', rotation=45, ha='right')
plt.yticks(fontsize=12, color='brown', rotation=0)

plt.show()
