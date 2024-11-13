# importing packages
import seaborn

# load dataset
data = seaborn.load_dataset('exercise')

# multiple groupby (pulse and diet both)
df = data.groupby(['pulse', 'diet']).count()['time']

# plot the result
df.unstack().plot()
plt.xticks(rotation=45)
plt.show()
