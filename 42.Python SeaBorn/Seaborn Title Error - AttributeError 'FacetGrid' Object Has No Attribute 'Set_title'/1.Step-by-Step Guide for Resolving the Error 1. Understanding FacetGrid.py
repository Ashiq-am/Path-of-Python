import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Create a FacetGrid
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True, despine=False)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.figure.subplots_adjust(wspace=0, hspace=0)
