chart = alt.Chart(geo_df).mark_geoshape(
    fill='lightgray',
    stroke='black',
    strokeWidth=0.5
).encode(
    tooltip='properties.name:N'
).project(
    type='mercator'
).properties(
    width=800,
    height=400
)
chart
