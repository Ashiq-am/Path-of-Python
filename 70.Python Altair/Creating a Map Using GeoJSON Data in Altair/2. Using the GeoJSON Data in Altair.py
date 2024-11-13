import altair as alt
import geopandas as gpd

# Load the random GeoJSON data
geo_df = gpd.read_file('random_geojson_data.geojson')

# Create a map using Altair
chart = alt.Chart(geo_df).mark_geoshape().encode(
    tooltip='name:N'
).project(
    type='mercator'
).properties(
    width=800,
    height=400
)

chart
