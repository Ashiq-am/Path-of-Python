# import libraray for creat choropleth map
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data and create a choropleth map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(column='gdp_md_est',
		cmap='OrRd', legend=True)

# Resize the plot
fig = plt.gcf()
fig.set_size_inches(12, 6)

# show map
plt.show()
