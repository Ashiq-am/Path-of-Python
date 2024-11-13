import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = {'col1': [1, 2, 3], 'col2': [3, 4, 5]}
df = pd.DataFrame(data)

# Define name mapping
name_mapping = {'col1': 'hello', 'col2': 'hi'}

# Create a line chart with additional features
fig = go.Figure()

# Add traces for each column
for col in df.columns:
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[col],
            mode='lines+markers',
            name=name_mapping[col] if col in name_mapping else col,
            line=dict(
                color='blue' if col == 'col1' else 'green',  # Custom line color
                dash='dash' if col == 'col1' else 'dot'      # Custom line style
            ),
            marker=dict(
                size=10,
                symbol='circle' if col == 'col1' else 'square',  # Custom marker style
                color='blue' if col == 'col1' else 'green'       # Custom marker color
            )
        )
    )

# Customize layout
fig.update_layout(
    title='Custom Line Chart with Updated Features',
    xaxis_title='Index',
    yaxis_title='Values',
    legend_title='Legend',
    plot_bgcolor='lightgray',
    font=dict(size=14)
)

# Show the updated plot
fig.show()
