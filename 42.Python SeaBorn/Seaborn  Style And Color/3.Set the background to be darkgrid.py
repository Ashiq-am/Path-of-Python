import seaborn as sns
import matplotlib.pyplot as plt

# load the tips dataset present by default in seaborn
tips = sns.load_dataset('tips')
sns.set_style('darkgrid')

# make a countplot
sns.countplot(x ='sex', data = tips)
