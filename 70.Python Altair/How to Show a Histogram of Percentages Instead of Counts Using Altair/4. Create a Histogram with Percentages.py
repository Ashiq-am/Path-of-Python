# Histogram showing percentages
histogram_percentage = alt.Chart(data).transform_bin(
    'binned_value', field='value'
).transform_aggregate(
    count='count()', groupby=['binned_value']
).transform_calculate(
    percentage='datum.count / sum(datum.count)'
).mark_bar().encode(
    alt.X('binned_value:Q', bin=alt.Bin(step=0.5), title='Value'),
    alt.Y('percentage:Q', axis=alt.Axis(format='%'), title='Percentage')
).properties(
    title='Histogram of Values (Percentages)'
)

histogram_percentage
