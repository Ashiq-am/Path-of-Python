import seaborn as sns

# Get the list of available datasets
datasets = sns.get_dataset_names()

for dataset in datasets:
    print(dataset)
