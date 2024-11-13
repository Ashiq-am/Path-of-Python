# importing packages
import seaborn

# load dataset
data = seaborn.load_dataset('exercise')

# multiple groupby (pulse, diet, and time)
df = data.groupby(['pulse', 'diet', 'time']).count()['kind']

# plot the result
df.unsatck().plot()
plt.xticks(rotation=30)
plt.show()
