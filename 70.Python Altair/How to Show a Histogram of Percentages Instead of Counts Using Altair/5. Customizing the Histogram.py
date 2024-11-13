# Customized histogram with percentages
histogram_custom = alt.Chart(data).transform_bin(
    'binned_value', field='value'
).transform_aggregate(
    count='count()', groupby=['binned_value']
).transform_calculate(
    percentage='datum.count / sum(datum.count)'
).mark_bar(color='teal').encode(
    alt.X('binned_value:Q', bin=alt.Bin(step=0.2), title='Value'),
    alt.Y('percentage:Q', axis=alt.Axis(format='%'), title='Percentage'),
    tooltip=['binned_value:Q', 'percentage:Q']
).properties(
    title='Customized Histogram of Values (Percentages)'
)

histogram_custom
