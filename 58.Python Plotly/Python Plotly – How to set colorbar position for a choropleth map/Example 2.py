# importing packages
import plotly.express as px

# using gapminder datasheet.
df = px.data.gapminder().query("year==2007")

# figure setup
fig = px.choropleth(df, locations="iso_alpha",

                    # lifeExp is a column of gapminder
                    color="lifeExp",

                    # column to add to hover information
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma)

# set colorbar position for Y-axis
fig.update_layout(coloraxis_colorbar_y=-0.3)

fig.show()
