bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:O',
    y='value:Q',
    color=alt.condition(
        alt.datum.value > 5,
        alt.value('orange'),  # If condition is true
        alt.value('steelblue')  # If condition is false
    )
)
bar_chart
