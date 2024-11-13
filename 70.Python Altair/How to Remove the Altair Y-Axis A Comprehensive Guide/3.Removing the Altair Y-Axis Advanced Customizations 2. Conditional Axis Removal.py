import altair as alt
from vega_datasets import data

iris = data.iris()

remove_y_axis = True

y_axis = alt.Y('petalLength', axis=None) if remove_y_axis else alt.Y('petalLength')

chart = alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y=y_axis,
    color='species'
)
chart
