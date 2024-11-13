chart = alt.Chart(cars).mark_point().encode(
    x=alt.X('Horsepower', axis=alt.Axis(title='Horsepower', labelFontSize=12, titleFontSize=14)),
    y=alt.Y('Miles_per_Gallon', axis=alt.Axis(title='Miles Per Gallon', labelFontSize=12, titleFontSize=14)),
    color='Origin'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

chart
