# Add sidelabels
fig.update_layout(
    annotations=[
        dict(text="Label 1", xref="paper", yref="paper", x=0.25, y=1.05, showarrow=False),
        dict(text="Label 2", xref="paper", yref="paper", x=0.75, y=1.05, showarrow=False),
        dict(text="Label 3", xref="paper", yref="paper", x=0.25, y=-0.1, showarrow=False),
        dict(text="Label 4", xref="paper", yref="paper", x=0.75, y=-0.1, showarrow=False)
    ]
)

fig.show()
