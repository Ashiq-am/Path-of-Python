import numpy as np
import plotly.graph_objects as go

# Step 1: Generate Data
np.random.seed(0)
x = np.arange(2000, 2025)
y = np.random.normal(loc=0, scale=1, size=len(x)).cumsum()
ci_upper = y + 1.96 * np.std(y) / np.sqrt(len(y))
ci_lower = y - 1.96 * np.std(y) / np.sqrt(len(y))

# Step 2: Create the Plotly Figure
fig = go.Figure()

# Add the main line
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='lines',
    name='Mean',
    line=dict(color='rgb(31, 119, 180)')
))

# Add the confidence interval
fig.add_trace(go.Scatter(
    x=np.concatenate([x, x[::-1]]),
    y=np.concatenate([ci_upper, ci_lower[::-1]]),
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo='skip',
    showlegend=False,
    name='95% CI'
))

# Step 3: Customize the Layout
fig.update_layout(
    title='Line Chart with 95% Confidence Interval',
    xaxis_title='Year',
    yaxis_title='Value',
    hovermode='x'
)

# Step 4: Display the Plot
fig.show()
