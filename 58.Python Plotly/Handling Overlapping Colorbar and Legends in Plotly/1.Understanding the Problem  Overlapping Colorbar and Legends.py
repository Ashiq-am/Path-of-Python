import plotly.express as px

# Sample data
data = {
    'Length.': [1, 2, 3],
    'Beats.Per.Minute': [120, 130, 140],
    'Popularity': [10, 20, 30],
    'Rank': [1, 2, 3],
    'Genre': ['A', 'B', 'C']
}

# Creating a scatter ternary plot
fig = px.scatter_ternary(
    data_frame=data,
    a='Length.',
    b='Beats.Per.Minute',
    c='Popularity',
    color='Rank',
    symbol='Genre',
    labels={'Length.': 'Len', 'Beats.Per.Minute': 'Beats'},
    color_continuous_midpoint=15,
    symbol_sequence=['circle-open-dot', 'cross-open', 'triangle-ne']
)

fig.show()
