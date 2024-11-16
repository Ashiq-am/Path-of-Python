# importing packages
import seaborn

# load dataset and view
data = seaborn.load_dataset('exercise')
print(data)

# multiple groupby (pulse and diet both)
df = data.groupby(['pulse', 'diet']).count()['time']
print(df)

# plot the result
df.plot()
plt.xticks(rotation=45)
plt.show()
