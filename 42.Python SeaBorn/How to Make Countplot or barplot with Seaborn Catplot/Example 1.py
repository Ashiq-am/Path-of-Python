# plot for count of passengers belonging
# to each gender
sns.catplot(x='sex', kind='count', data=data)
plt.xlabel("Gender")
plt.ylabel("Count")
