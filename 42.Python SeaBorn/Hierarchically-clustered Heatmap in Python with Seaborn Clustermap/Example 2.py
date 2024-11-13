# Importing the library
import seaborn as sns
from sunbird.categorical_encoding import frequency_encoding

# Load dataset
data = sns.load_dataset('flights')

# Categorical encoding
frequency_encoding(data, 'month')

# Clustering data row-wise and
# changing color of the map.
sns.clustermap(data, cmap='coolwarm', figsize=(7, 7))
