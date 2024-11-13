import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.lmplot(x ='total_bill', y ='tip', size = 2, aspect = 4, data = tips)
