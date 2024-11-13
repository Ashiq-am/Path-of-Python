import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'Score': [33, 24, 29, 25, 30, 29, 34, 37],
    'Player': ['X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y']
})

# Create a boxplot
sns.boxplot(data=data, x='Player', y='Score')
plt.show()
