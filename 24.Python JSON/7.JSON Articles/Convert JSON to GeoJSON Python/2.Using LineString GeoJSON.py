import geojson

linestring_data = {"coordinates": [(0, 0), (1, 1), (2, 2)]}

# Creating a GeoJSON LineString
linestring_geojson = geojson.LineString(coordinates=linestring_data["coordinates"])

# Creating a FeatureCollection with the LineString
feature_collection = geojson.FeatureCollection(features=[geojson.Feature(geometry=linestring_geojson)])

# Printing the output
print(geojson.dumps(feature_collection, indent=2))
