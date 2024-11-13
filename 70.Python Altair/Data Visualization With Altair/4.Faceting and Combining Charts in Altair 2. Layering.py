stocks = data.stocks()
line = alt.Chart(stocks).mark_line().encode(
    x='date:T',
    y='price',
    color='symbol'
)

points = alt.Chart(stocks).mark_point().encode(
    x='date:T',
    y='price',
    color='symbol'
)

layered_chart = line + points
layered_chart
