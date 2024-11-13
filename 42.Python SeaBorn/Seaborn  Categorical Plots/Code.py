# import the seaborn libaray
import seaborn as sns

# import done to avoid warnings
from warnings import filterwarnings

# reading the dataset
df = sns.load_dataset('tips')

# first five entries if the dataset
df.head()
