import seaborn

seaborn.set(style='whitegrid')
tip = seaborn.load_dataset('tips')

seaborn.violinplot(x='day', y='tip', data=tip)
