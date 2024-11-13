# Import Library
import seaborn as sns

# style must be one of white, dark,
# whitegrid, darkgrid (Optional)
sns.set_style("darkgrid")

# Loading default data of seaborn
exercise = sns.load_dataset("exercise")
g = sns.FacetGrid(exercise, row="diet",
                  col="time", margin_titles=True)

g.map(sns.regplot, "id", "pulse", color=".3")

# Set Title for each subplot
col_order = ['Deltaic', 'Plains', 'Hummock',
             'Swale', 'Sand Dunes', 'Mountain']

# embeding center-text with its title
# using loop.
for txt, title in zip(g.axes.flat, col_order):
    txt.set_title(title)

    # add text
    txt.text(10, 120, 'Geeksforgeeks', fontsize=12)
