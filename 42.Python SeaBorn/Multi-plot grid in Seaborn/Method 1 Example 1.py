# loading of a dataframe from seaborn
exercise = sns.load_dataset("exercise")

# Form a facetgrid using columns
sea = sns.FacetGrid(exercise, col = "time")
