# Bar chart with increased bar width
bar_chart_wide = alt.Chart(data).mark_bar(size=60).encode(
    x='category:N',
    y='value:Q'
).properties(
    title='Bar Chart with Increased Bar Width'
)

bar_chart_wide
