import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset('fmri')

sns.lineplot(data=data, x='timepoint', y='signal', hue='region',ci=None)
plt.xlabel('Timepoint')
plt.ylabel('Signal')
plt.title('FMRI Signal Over Time by Region')
plt.show()
