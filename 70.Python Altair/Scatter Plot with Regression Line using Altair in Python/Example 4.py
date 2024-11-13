# importing libraries
import altair as alt
from vega_datasets import data

# importing weather dataset from vega_datasets package
weather_data = data.seattle_weather()

# making the scatter on temp_max and temp_min
fig = alt.Chart(weather_data).mark_point().encode(
x='temp_max',y='temp_min',color='weather')

# making the regression line using transform_regression
# function and add with the scatter plot
final_plot = fig + fig.transform_regression('temp_max','temp_min').mark_line()

# saving the scatter plot with regression line
final_plot.save('output4.html')
