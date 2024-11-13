# import Library
import seaborn as sns
import pandas as pd

# style must be one of white, dark,
# whitegrid, darkgrid
sns.set_style("darkgrid")

# Loading default data of seaborn
exercise = sns.load_dataset("exercise")
g = sns.FacetGrid(exercise, col="time",
                  height=4, aspect=.5)

g.map(sns.barplot, "diet", "pulse",
      order=["no fat", "low fat"])

# Set Title for each subplot
col_order = ['Deltaic Plains', 'Hummock and Swale',
             'Sand Dunes']

# embeding center-text with its title
# at each itteration
for txt, title in zip(g.axes.flat, col_order):
    txt.set_title(title)

    # add text
    txt.text(-0.2, 60, 'Geeksforgeeks', fontsize=12)
