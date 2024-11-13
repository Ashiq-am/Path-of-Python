import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 11, 12], name="Trace 1"), secondary_y=False)
fig.add_trace(go.Scatter(x=[2, 3, 4], y=[20, 21, 22], name="Trace 2", xaxis='x2'), secondary_y=False)
fig.add_trace(go.Scatter(x=[3, 4, 5], y=[30, 31, 32], name="Trace 3", xaxis='x3'), secondary_y=False)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="Trace 4"), secondary_y=True)

fig.update_layout(
    xaxis=dict(domain=[0, 0.45], title_text="Primary X-Axis"),
    xaxis2=dict(domain=[0.55, 1], anchor='y', overlaying='x', side='top', title_text="Secondary X-Axis"),
    xaxis3=dict(domain=[0.55, 1], anchor='y', overlaying='x', side='bottom', position=0.15, title_text="Tertiary X-Axis"),
    yaxis=dict(title_text="Primary Y-Axis"),
    yaxis2=dict(title_text="Secondary Y-Axis", overlaying='y', side='right')
)

fig.show()
