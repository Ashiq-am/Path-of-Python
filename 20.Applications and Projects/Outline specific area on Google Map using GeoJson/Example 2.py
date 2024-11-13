import folium


# provide path of ouline.json
# file that is in the data folder
outline = 'outline.json'

folium.GeoJson(outline, name ="madhyapradesh").add_to(map)

map
