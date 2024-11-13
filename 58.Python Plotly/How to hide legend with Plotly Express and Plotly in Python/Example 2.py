import plotly.graph_objects as go

# using the Figure dataset
fig = go.Figure()

fig.add_trace(go.Line(name="first", x=["a", "b"], y=[1,3]))
fig.add_trace(go.Line(name="second", x=["a", "b"], y=[2,1]))
fig.add_trace(go.Line(name="third", x=["a", "b"], y=[1,2]))
fig.add_trace(go.Line(name="fourth", x=["a", "b"], y=[2,3]))


# hiding legend in pyplot express.
fig.update(layout_showlegend=False)

fig.show()
