# Combine the two charts using hconcat
combined_chart = alt.hconcat(
    chart1,
    chart2
).resolve_scale(
    color='independent'  # Ensure that the color scales are independent
).properties(
    title='Combined Chart with Two Different Legends'
)

combined_chart
