# Python program to illustrate
# violinplot using inbuilt data-set
# given in seaborn

# importing the required module
import seaborn

# use to set style of background of plot
seaborn.set(style='whitegrid')

# loading data-set
tip = seaborn.load_dataset('tips')
plt.figure(figsize=(4, 7))

seaborn.violinplot(x='day', y='tip',
                   data=tip,
                   inner="stick")
