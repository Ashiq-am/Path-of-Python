# importing packages
import seaborn

# load data
tip = seaborn.load_dataset('tips')

# create catplot facetplot object
seaborn_facetgrid_object = seaborn.catplot(
	x='sex',
	y='tip',
	data=tip
)
# show plot
seaborn_facetgrid_object
