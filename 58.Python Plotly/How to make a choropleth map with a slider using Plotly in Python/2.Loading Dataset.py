df = pd.read_csv('https://raw.githubusercontent\
.com/plotly/datasets/master/2011_us_ag_exports.csv')

data = [dict(type='choropleth',
			locations = df['code'].astype(str),
			z=df['total exports'].astype(float),
			locationmode='USA-states')]
