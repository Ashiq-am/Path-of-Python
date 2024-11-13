# import folium package
import folium

# Map method of folium return Map object
# Here we pass coordinates of location
# to view on map and starting Zoom level = 4

map = folium.Map(location=[28.704060, 77.102493],zoom_start=4)

map
