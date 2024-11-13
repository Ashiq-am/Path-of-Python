chart = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
).properties(
    title=alt.TitleParams(
        text='Cars Data',
        subtitle='Analysis of Horsepower vs. Miles per Gallon',
        fontSize=16,
        font='Courier',
        color='gray',
        subtitleFontSize=12,
        subtitleFontStyle='italic',
        subtitleColor='darkgray'
    )
)
chart
