# importing libraries
import altair as alt
from vega_datasets import data

# importing airports dataset from
# vega_datasets package
airport = data.airports()

# making the scatter plot on latitude and longitude
fig = alt.Chart(airport).mark_point().encode(x='latitude',y='longitude')

# making the regression line using transform_regression
# function and add with the scatter plot
final_plot = fig + fig.transform_regression('latitude','longitude').mark_line()

# saving the scatter plot with regression line
final_plot.save('output1.html')
