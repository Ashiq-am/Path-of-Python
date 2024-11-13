import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
plt.figure(figsize =(12, 3))
sns.countplot(x ='sex', data = tips)
