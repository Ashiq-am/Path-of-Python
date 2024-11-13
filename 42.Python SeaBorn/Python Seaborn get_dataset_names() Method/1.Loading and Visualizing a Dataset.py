import seaborn as sns

# Get the list of available datasets
datasets = sns.get_dataset_names()

# Load the 'iris' dataset
iris = sns.load_dataset('iris')

print(iris.head())
