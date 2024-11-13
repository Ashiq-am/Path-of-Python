app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input',
              value='Enter a number',
              type='text'),

    html.Div(id='output')
])
