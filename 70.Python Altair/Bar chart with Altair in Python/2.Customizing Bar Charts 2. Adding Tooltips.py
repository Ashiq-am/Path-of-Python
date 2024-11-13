bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:O',
    y='value:Q',
    tooltip=['category', 'value']
)
bar_chart
