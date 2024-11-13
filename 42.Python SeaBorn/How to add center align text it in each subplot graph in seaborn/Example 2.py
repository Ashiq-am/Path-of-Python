# import Library
import seaborn as sns
import pandas as pd

# style must be one of white, dark,
# whitegrid, darkgrid (Optional)
sns.set_style("darkgrid")

# Loading default data of seaborn
exercise = sns.load_dataset("exercise")
exercise_kind = exercise.kind.value_counts().index

g = sns.FacetGrid(exercise, row="kind",
                  row_order=exercise_kind,
                  height=1.7, aspect=4, )
g.map(sns.kdeplot, "id")

# Set Title
col_order = ['Deltaic Plains', 'Hummock and Swale',
             'Sand Dunes']

# embeding center-text with its title
# at each itteration
for txt, title in zip(g.axes.flat, col_order):
    txt.set_title(title)

    # add text
    txt.text(10.58, 0.04, 'Geeksforgeeks', fontsize=11)
