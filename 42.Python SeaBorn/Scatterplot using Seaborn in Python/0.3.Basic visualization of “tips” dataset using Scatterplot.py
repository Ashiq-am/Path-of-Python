import seaborn


seaborn.set(style='whitegrid')
tip = seaborn.load_dataset('tips')

seaborn.scatterplot(x='day', y='tip', data=tip)
