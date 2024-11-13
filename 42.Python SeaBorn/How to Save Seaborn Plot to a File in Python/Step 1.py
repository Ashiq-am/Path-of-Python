# code
# Install seaborn using pip install seaborn
# Import the seaborn package
import seaborn as sns

# load the inbuilt "penguins" dataset using
# seaborn inbuilt function load_dataset
data = sns.load_dataset("penguins")

# print the first 6 data
data.head()
