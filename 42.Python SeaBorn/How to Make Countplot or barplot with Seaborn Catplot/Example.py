# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# setting background style
sns.set_style('darkgrid')

# import dataset
data = sns.load_dataset('titanic')
data.head()
