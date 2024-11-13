import geojson

# JSON data representing coordinates of a Polygon
polygon_data = {"coordinates": [[(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]]}

# Creating a GeoJSON Polygon geometry
polygon_geojson = geojson.Polygon(coordinates=polygon_data["coordinates"])

#Printing the Output...
print(geojson.dumps(polygon_geojson, indent=2))
