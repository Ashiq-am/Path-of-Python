# Import Library
import seaborn as sns
import pandas as pd

# style must be one of white,
# dark, whitegrid, darkgrid
sns.set_style("darkgrid")

# Loading default data of seaborn
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, row="sex",
                  col="smoker",
                  margin_titles=True)
g.map(sns.lineplot, "total_bill", 'tip')

# Set Title for each subplot
col_order = ['Deltaic Plains', 'Hummock and Swale',
             'Sand Dunes', 'Mountain']

# embeding center-text with its
# title at each itteration
for txt, title in zip(g.axes.flat, col_order):
    txt.set_title(title)

    # add text
    txt.text(15, 6, 'Geeksforgeeks', fontsize=12)
