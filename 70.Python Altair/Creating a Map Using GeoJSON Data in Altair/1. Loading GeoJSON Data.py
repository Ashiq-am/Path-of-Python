import json
import random

# Function to generate random coordinates
def generate_random_coordinates(num_points):
    return [[random.uniform(-180, 180), random.uniform(-90, 90)] for _ in range(num_points)]

# Generating random GeoJSON data
random_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": f"Random Feature {i}"
            },
            "geometry": {
                "type": "Point",
                "coordinates": generate_random_coordinates(1)[0]  # Single random point
            }
        } for i in range(10)  # 10 random points
    ]
}

# Save to file
with open('random_geojson_data.geojson', 'w') as f:
    json.dump(random_geojson, f)

# Output the random GeoJSON data
print(json.dumps(random_geojson, indent=2))
