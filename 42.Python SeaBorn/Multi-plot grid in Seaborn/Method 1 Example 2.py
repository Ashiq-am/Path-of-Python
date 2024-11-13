# Form a facetgrid using columns with a hue
sea = sns.FacetGrid(exercise, col="time", hue="kind")

# map the above form facetgrid with some attributes
sea.map(sns.scatterplot, "pulse", "time", alpha=.8)

# adding legend
sea.add_legend()
