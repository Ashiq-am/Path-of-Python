import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
data = sns.load_dataset("fmri")

# Adjust transparency of the confidence interval
sns.relplot(
    x="timepoint",
    y="signal",
    kind="line",
    data=data,
    ci=95,  # Show the confidence interval (default is 95)
)
# Access the underlying matplotlib Axes object
ax = plt.gca()
# Find the line representing the confidence interval and adjust its alpha
for line in ax.lines:
    if line.get_label() == '_ci':  # This assumes the CI line has label '_ci'
        line.set_alpha(0.8)

plt.show()
