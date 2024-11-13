# import library & dataset
import seaborn as sns


df = sns.load_dataset('iris')

# Just switch x and y
sns.boxplot(y=df["species"], x=df["sepal_length"])
