# import the necesssary packages
import folium
import pandas as pd

# importing the dataset as a csv file,
# and storing it as a dataframe in 'df'
df = pd.read_csv('Volcanoes.txt')

# calculating the mean of the latitudes
# and longitudes of the locations of volcanoes
latmean = df['LAT'].mean()
lonmean = df['LON'].mean()

# Creating a map object using Map() function.
# Location parameter takes latitudes and
# longitudes as starting location.
# (Map will be centered at those co-ordinates)
map5 = folium.Map(location=[latmean, lonmean],
                  zoom_start=6, tiles='Mapbox bright')


# Function to change the marker color
# according to the elevation of volcano
def color(elev):
    if elev in range(0, 1000):
        col = 'green'
    elif elev in range(1001, 1999):
        col = 'blue'
    elif elev in range(2000, 2999):
        col = 'orange'
    else:
        col = 'red'
    return col


# Iterating over the LAT,LON,NAME and
# ELEV columns simultaneously using zip()
for lat, lan, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    # Marker() takes location coordinates
    # as a list as an argument
    folium.Marker(location=[lat, lan], popup=name,
                  icon=folium.Icon(color=color(elev),
                                   icon_color='yellow', icon='cloud')).add_to(map5)

# Save the file created above
print(map5.save('test7.html'))
