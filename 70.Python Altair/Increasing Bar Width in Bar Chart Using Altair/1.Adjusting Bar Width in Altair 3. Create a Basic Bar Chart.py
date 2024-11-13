# Basic bar chart
bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q'
).properties(
    title='Basic Bar Chart'
)

bar_chart
