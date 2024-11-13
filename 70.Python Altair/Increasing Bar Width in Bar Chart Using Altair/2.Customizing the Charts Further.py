# Customized bar chart with increased bar width and colors
bar_chart_custom = alt.Chart(data).mark_bar(size=60, color='teal').encode(
    x=alt.X('category:N', title='Category'),
    y=alt.Y('value:Q', title='Value'),
    tooltip=['category:N', 'value:Q']
).properties(
    title='Customized Bar Chart with Increased Bar Width'
)

bar_chart_custom
