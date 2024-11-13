import plotly.express as px

# Sample data
z = [[.1, .3, .5], [1.0, .8, .6], [.6, .4, .2]]
z_text = [['Low', 'Medium', 'High'], ['Very High', 'High', 'Medium'], ['Medium', 'Low', 'Very Low']]

# Create annotated heatmap
fig = px.imshow(z, text_auto=True, color_continuous_scale='Viridis')
fig.update_traces(text=z_text, texttemplate="%{text}")
fig.show()
