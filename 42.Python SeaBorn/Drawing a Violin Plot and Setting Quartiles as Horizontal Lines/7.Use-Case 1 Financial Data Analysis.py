import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample dataset
data = {
    "fund": ["Fund A"] * 100 + ["Fund B"] * 100 + ["Fund C"] * 100,
    "quarterly_return": np.random.normal(0.05, 0.02, 100).tolist() +
                        np.random.normal(0.07, 0.03, 100).tolist() +
                        np.random.normal(0.04, 0.015, 100).tolist()
}

df = pd.DataFrame(data)

# Create a violin plot with quartile lines
sns.violinplot(x="fund", y="quarterly_return", data=df, inner="quartile")
plt.title("Quarterly Returns Distribution by Fund")
plt.xlabel("Mutual Fund")
plt.ylabel("Quarterly Return (%)")
plt.show()
