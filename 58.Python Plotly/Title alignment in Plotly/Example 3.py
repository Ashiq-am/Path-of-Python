# import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
df = pd.DataFrame({
	"Year": ["2015", "2016", "2017", "2015", "2016", "2017"],
	"Revenue": [4, 1, 2, 2, 4, 5],
	"Company": ["ABC Pvt. Ltd.", "ABC Pvt. Ltd.", "ABC Pvt. Ltd.", "XYZ Pvt. Ltd.", "XYZ Pvt. Ltd.", "XYZ Pvt. Ltd."]
})

# depict visualization
fig = px.bar(df, x="Year", y="Revenue", color="Company", barmode="group")

app.layout = html.Div(children=[

	dcc.Graph(
		id='example-graph',
		figure=fig
	)
])

# allign title
fig.update_layout(title_text='Revenue', title_x=0.5)

if __name__ == '__main__':
	app.run_server(debug=True)
