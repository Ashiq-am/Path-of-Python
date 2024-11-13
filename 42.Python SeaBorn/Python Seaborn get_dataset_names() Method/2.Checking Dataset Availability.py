import seaborn as sns

# Get the list of available datasets
datasets = sns.get_dataset_names()

if 'titanic' in datasets:
    print("The 'titanic' dataset is available.")
else:
    print("The 'titanic' dataset is not available.")
