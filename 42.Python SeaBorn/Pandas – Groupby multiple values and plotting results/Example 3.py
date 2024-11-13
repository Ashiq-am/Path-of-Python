# importing packages
import seaborn

# load dataset and view
data = seaborn.load_dataset('exercise')
print(data)

# multiple groupby (pulse, diet and time)
df = data.groupby(['pulse', 'diet', 'time']).count()['kind']
print(df)

# plot the result
df.plot()
plt.xticks(rotation=30)
plt.show()
