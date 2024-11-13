import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    name='Set A',
    x=['Val x', 'Val y', 'Val z'], y=[6, 4, 3],
    error_y=dict(type='data', array=[1, 0.5, 1.5]),
    width=0.15
))
fig.add_trace(go.Bar(
    name='Set B',
    x=['Val x', 'Val y', 'Val z'], y=[2, 9, 5],
    error_y=dict(type='data', array=[0.5, 1, 2]),
    width=0.15
))
fig.update_layout(barmode='group',
                  title=dict(
                      text="Plotly <br> Graph <br> Title Overlap",
                      x=0.5,
                      y=0.95,
                      xanchor='center',
                      yanchor='top',
                      # pad = dict(
                      #		 t = 0
                      #		 ),
                      font=dict(

                          # family='Courier New, monospace',
                          size=40,
                          # color='#000000'
                      )
                  ))

fig.show()
