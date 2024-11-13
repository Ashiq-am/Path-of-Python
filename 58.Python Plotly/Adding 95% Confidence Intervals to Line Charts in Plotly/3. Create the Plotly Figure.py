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
