bar_chart = alt.Chart(data).mark_bar(color='skyblue').encode(
    x='category:O',
    y='value:Q'
)
bar_chart
