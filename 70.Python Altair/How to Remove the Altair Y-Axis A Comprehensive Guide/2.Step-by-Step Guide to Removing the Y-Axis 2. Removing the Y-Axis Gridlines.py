import altair as alt
from vega_datasets import data

iris = data.iris()

chart = alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y=alt.Y('petalLength', axis=None),
    color='species'
).configure_axis(
    grid=False
)
chart
