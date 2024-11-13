# Bar chart with adjusted width to prevent overlapping
bar_chart_no_overlap = alt.Chart(data).mark_bar(size=100).encode(
    x=alt.X('category:N', title='Category'),
    y=alt.Y('value:Q', title='Value')
).properties(
    width=400,
    title='Bar Chart with Increased Width to Prevent Overlapping'
)

bar_chart_no_overlap
