# import the graph_objects function from
# plotly package
import plotly.graph_objects as go

# initialize a Figure object and store it in
# a variable fig
fig = go.Figure()

# add x and y values for the 1st scatter
# plot and name the yaxis as yaxis1 values
fig.add_trace(go.Scatter(
    x=[10, 12, 13],
    y=[41, 58, 60],
    name="yaxis1 values"
))

# add x and y values for the 2nd scatter
# plot and name the yaxis as yaxis2 values
fig.add_trace(go.Scatter(
    x=[12, 13, 14],
    y=[401, 501, 610],
    name="yaxis2 values",
    yaxis="y2"
))

# add x and y values for the 3rd scatter
# plot and name the yaxis as yaxis3 values
fig.add_trace(go.Scatter(
    x=[14, 15, 16],
    y=[42000, 53000, 65000],
    name="yaxis3 values",
    yaxis="y3"
))

# add x and y values for the 4th scatter plot
# and name the yaxis as yaxis4 values
fig.add_trace(go.Scatter(
    x=[15, 16, 17],
    y=[2000, 5000, 7000],
    name="yaxis4 values",
    yaxis="y4"
))

# Create axis objects
fig.update_layout(
    # split the x-axis to fraction of plots in
    # proportions
    xaxis=dict(
        domain=[0.3, 0.7]
    ),

    # pass the y-axis title, titlefont, color
    # and tickfont as a dictionary and store
    # it an variable yaxis
    yaxis=dict(
        title="yaxis 1",
        titlefont=dict(
            color="#0000ff"
        ),
        tickfont=dict(
            color="#0000ff"
        )
    ),

    # pass the y-axis 2 title, titlefont, color and
    # tickfont as a dictionary and store it an
    # variable yaxis 2
    yaxis2=dict(
        title="yaxis 2",
        titlefont=dict(
            color="#FF0000"
        ),
        tickfont=dict(
            color="#FF0000"
        ),
        anchor="free",  # specifying x - axis has to be the fixed
        overlaying="y",  # specifyinfg y - axis has to be seperated
        side="left",  # specifying the side the axis should be present
        position=0.2  # specifying the position of the axis
    ),

    # pass the y-axis 3 title, titlefont, color and
    # tickfont as a dictionary and store it an
    # variable yaxis 3
    yaxis3=dict(
        title="yaxis 3",
        titlefont=dict(
            color="#006400"
        ),
        tickfont=dict(
            color="#006400"
        ),
        anchor="x",  # specifying x - axis has to be the fixed
        overlaying="y",  # specifyinfg y - axis has to be seperated
        side="right"  # specifying the side the axis should be present
    ),

    # pass the y-axis 4 title, titlefont, color and
    # tickfont as a dictionary and store it an
    # variable yaxis 4
    yaxis4=dict(
        title="yaxis 4",
        titlefont=dict(
            color="#8f00ff"
        ),
        tickfont=dict(
            color="#8f00ff"
        ),
        anchor="free",  # specifying x - axis has to be the fixed
        overlaying="y",  # specifyinfg y - axis has to be seperated
        side="right",  # specifying the side the axis should be present
        position=0.8  # specifying the position of the axis
    )
)

# Update layout of the plot namely title_text, width
# and place it in the center using title_x parameter
# as shown
fig.update_layout(
    title_text="4 y-axes scatter plot in plotly",
    width=1000,
    title_x=0.5
)
