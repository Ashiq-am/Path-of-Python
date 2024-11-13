# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv('homelessness.csv')

# plotting two histograms on the same axis
plt.hist(df['individuals'], bins=25, alpha=0.45, color='red')
plt.hist(df['family_members'], bins=25, alpha=0.45, color='blue')

plt.title("histogram with multiple \
variables (overlapping histogram)")

plt.legend(['individuals who are homeless',
			'family members who are homeless'])

plt.show()
