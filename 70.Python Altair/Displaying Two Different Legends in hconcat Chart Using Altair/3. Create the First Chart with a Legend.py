# First bar chart with legend
chart1 = alt.Chart(data).mark_bar().encode(
    x=alt.X('category:N', title='Category'),
    y=alt.Y('value1:Q', title='Value 1'),
    color=alt.Color('category:N', legend=alt.Legend(title='Category Legend 1'))
).properties(
    title='Bar Chart 1'
)
