import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
data = sns.load_dataset("fmri")

# Create a line plot using relplot
sns.relplot(x="timepoint", y="signal", kind="line", data=data)

plt.show()
