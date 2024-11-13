fig = go.Figure(data=[go.Sankey(
    node=dict(
        thickness=5,
        line=dict(color="green", width=0.1),
        label=["A", "B", "C", "D", "E", "F"],
        color="blue"
    ),
    link=dict(

        # indices correspond to labels
        source=[0, 6, 1, 4, 2, 3],
        target=[2, 1, 5, 2, 1, 5],
        value=[7, 1, 3, 6, 9, 4]
    ))])

fig.update_layout(
    hovermode='x',
    title="Sankey Diagram",
    font=dict(size=10, color='green'),
    plot_bgcolor='blue',
    paper_bgcolor='yellow'
)

fig.show()
