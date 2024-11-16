# Draw a vertical boxplot grouped
# by a categorical variable:
import sns as sns

sns.set_style("whitegrid")

sns.boxplot(x = 'day', y = 'total_bill', data = tips)
