# Highlight the NaN values in DataFrame
# using seaborn color palette as well as
# min('lighblue') and max('blue') values
# in each column
print("\nModified Stlying DataFrame:")
df.style.background_gradient(cmap=cm).set_precision(2).highlight_null('red').highlight_min(axis=0, color='lightblue').highlight_max(axis=0, color='blue')
