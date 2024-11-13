fig.update_layout(
    xaxis=dict(
        title='X1 Axis',
        domain=[0, 1],
        anchor='y'
    ),
    xaxis2=dict(
        title='X2 Axis',
        domain=[0, 1],
        anchor='y',
        overlaying='x'
    ),
    xaxis3=dict(
        title='X3 Axis',
        domain=[0, 1],
        anchor='y',
        overlaying='x'
    ),
    yaxis=dict(
        title='Y Axis'
    )
)
fig.show()
