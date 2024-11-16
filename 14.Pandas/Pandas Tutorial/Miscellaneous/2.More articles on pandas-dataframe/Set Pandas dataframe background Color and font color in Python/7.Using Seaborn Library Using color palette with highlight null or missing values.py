# Highlight the NaN values in DataFrame
# using seaborn color palette
print("\nModified Stlying DataFrame:")
df.style.background_gradient(cmap=cm).set_precision(2).highlight_null('red')
