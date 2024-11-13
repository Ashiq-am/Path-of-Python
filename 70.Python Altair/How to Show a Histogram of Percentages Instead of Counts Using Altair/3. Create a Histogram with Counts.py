# Standard histogram showing counts
histogram = alt.Chart(data).mark_bar().encode(
    alt.X('value:Q', bin=True, title='Value'),
    alt.Y('count()', title='Count')
).properties(
    title='Histogram of Values (Counts)'
)

histogram
