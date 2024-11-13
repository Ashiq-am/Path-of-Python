import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({'Year': [2021, 2022, 2023], 'Sales': [100, 200, 300]})

plt.plot(df['Year'], df['Sales'])
plt.xticks(df['Year'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Year vs Sales')
plt.show()
