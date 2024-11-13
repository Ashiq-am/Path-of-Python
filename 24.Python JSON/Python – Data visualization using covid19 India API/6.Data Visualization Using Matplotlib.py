# plotting of data
plt.bar(dis, df['Active'], width=0.5, align='center')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.xticks(rotation=75)
plt.show()
print('*'*100)
