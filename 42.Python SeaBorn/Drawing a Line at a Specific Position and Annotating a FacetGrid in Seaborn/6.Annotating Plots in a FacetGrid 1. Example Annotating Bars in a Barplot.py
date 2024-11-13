import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create a FacetGrid with barplots
g = sns.FacetGrid(tips, col="smoker", height=5, aspect=1.5)
g.map(sns.barplot, "sex", "total_bill", palette='viridis', order=['Male', 'Female'])

# Annotate bars
for ax in g.axes.flat:
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2., p.get_height(), '{:.1f}'.format(p.get_height()),
                ha='center', va='center', fontsize=12, color='black', rotation=0)

# Show the plot
plt.show()
