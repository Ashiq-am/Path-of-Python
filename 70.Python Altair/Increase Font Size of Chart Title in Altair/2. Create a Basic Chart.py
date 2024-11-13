chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value'
).properties(
    title='Sample Chart Title'
)
