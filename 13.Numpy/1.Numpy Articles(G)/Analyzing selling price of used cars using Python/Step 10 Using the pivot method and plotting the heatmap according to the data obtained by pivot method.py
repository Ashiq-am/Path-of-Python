# pivot method
data_pivot = data_grp.pivot(index = 'drive-wheels',
							columns = 'body-style')
data_pivot

# heatmap for visualizing data
plt.pcolor(data_pivot, cmap ='RdBu')
plt.colorbar()
plt.show()
