import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.countplot(x ='sex', data = tips)
sns.despine()
