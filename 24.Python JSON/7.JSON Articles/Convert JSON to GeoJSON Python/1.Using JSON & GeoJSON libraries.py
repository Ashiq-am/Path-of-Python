import json
import geojson

def convert_json_to_geojson(json_data):
	#Parsing JSON data
	parsed_json = json.loads(json_data)

	# Converting to GeoJSON feature
	feature = geojson.Feature(geometry=parsed_json["geometry"], properties=parsed_json["properties"])

	#Create a GeoJSON FeatureCollection
	feature_collection = geojson.FeatureCollection([feature])
	return feature_collection

example_json_data = '''
{
"type": "Feature",
"properties": {
	"name": "Example Feature"
},
"geometry": {
	"type": "Point",
	"coordinates": [0, 0]
}
}
'''
# Converting JSON to GeoJSON
geojson_result = convert_json_to_geojson(example_json_data)

#Printing the GeoJSON result.
print(geojson.dumps(geojson_result, indent=2))
