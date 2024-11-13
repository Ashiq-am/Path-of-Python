import seaborn as sns

# Load Iris dataset
iris_df = sns.load_dataset('iris')

# Visualize using pairplot
sns.pairplot(iris_df, hue='species')
