# Second bar chart with legend
chart2 = alt.Chart(data).mark_bar().encode(
    x=alt.X('category:N', title='Category'),
    y=alt.Y('value2:Q', title='Value 2'),
    color=alt.Color('value2:Q', legend=alt.Legend(title='Value 2 Legend'), scale=alt.Scale(scheme='blues'))
).properties(
    title='Bar Chart 2'
)
