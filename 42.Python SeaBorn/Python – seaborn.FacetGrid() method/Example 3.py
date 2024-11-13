# importing packages
import seaborn
import matplotlib.pyplot as plt

# loading of a dataframe from seaborn
df = seaborn.load_dataset('tips')

############# Main Section		 #############
# Form a facetgrid using columns with a hue
graph = seaborn.FacetGrid(df, col ='time', hue ='smoker')
# map the above form facetgrid with some attributes
graph.map(seaborn.regplot, "total_bill", "tip").add_legend()
# show the object
plt.show()

# This code is contributed by Deepanshu Rustagi.
