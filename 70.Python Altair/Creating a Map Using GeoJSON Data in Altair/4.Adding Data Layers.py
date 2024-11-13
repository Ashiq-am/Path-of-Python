import altair as alt
import geopandas as gpd
import pandas as pd
import json
import random

# Load the random GeoJSON data
with open('random_geojson_data.geojson', 'r') as f:
    random_geojson = json.load(f)

# Create a GeoDataFrame from the GeoJSON data
geo_df = gpd.GeoDataFrame.from_features(random_geojson['features'])

# Generate random population density data
random_points = {
    'name': [f'Feature {i}' for i in range(10)],
    'population_density': [random.randint(1, 100) for _ in range(10)],  # Random values between 1 and 100
    'longitude': [feature['geometry']['coordinates'][0] for feature in random_geojson['features']],
    'latitude': [feature['geometry']['coordinates'][1] for feature in random_geojson['features']]
}

population_df = pd.DataFrame(random_points)

# Create the base map using GeoJSON data
base_map = alt.Chart(geo_df).mark_geoshape(
    fill='lightgray',
    stroke='black',
    strokeWidth=0.5
).encode(
    tooltip='name:N'
).project(
    type='mercator'
).properties(
    width=800,
    height=400
)

# Create a layer of points with population density data
points_layer = alt.Chart(population_df).mark_circle(size=100).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='population_density:Q',
    tooltip=['name:N', 'population_density:Q']
)

# Combine the base map and points layer
layered_map = base_map + points_layer

layered_map
