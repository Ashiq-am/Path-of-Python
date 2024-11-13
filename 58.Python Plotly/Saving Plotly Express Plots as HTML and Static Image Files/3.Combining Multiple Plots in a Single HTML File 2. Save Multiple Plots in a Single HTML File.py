from plotly.subplots import make_subplots

# Create a subplot figure
fig = make_subplots(rows=1, cols=2)

# Add the first plot to the subplot
for trace in fig1.data:
    fig.add_trace(trace, row=1, col=1)

# Add the second plot to the subplot
for trace in fig2.data:
    fig.add_trace(trace, row=1, col=2)

# Save the subplot as an HTML file
fig.write_html("combined_plots.html")
