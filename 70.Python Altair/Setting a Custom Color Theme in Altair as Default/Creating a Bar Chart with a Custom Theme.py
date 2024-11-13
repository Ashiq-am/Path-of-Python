import altair as alt
import pandas as pd

# Define the custom theme
def my_custom_theme():
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "mark": {"color": "steelblue"},
            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "labelColor": "gray",
                "titleColor": "black"
            },
            "range": {
                "category": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
            }
        }
    }

# Register and enable the custom theme
alt.themes.register('my_custom_theme', my_custom_theme)
alt.themes.enable('my_custom_theme')

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 15, 13, 17, 9]
})

# Create a bar chart
chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value',
    color='Category'
)

# Display the chart
chart.show()
