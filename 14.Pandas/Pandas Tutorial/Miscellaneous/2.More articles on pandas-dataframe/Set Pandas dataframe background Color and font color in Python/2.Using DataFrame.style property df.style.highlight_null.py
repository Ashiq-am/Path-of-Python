# Replacing the locating value by NaN (Not a Nummber)
df.iloc[0, 3] = np.nan
df.iloc[2, 3] = np.nan
df.iloc[4, 2] = np.nan
df.iloc[7, 4] = np.nan

# Highlight the NaN values in DataFrame
print("\nModified Stlying DataFrame:")
df.style.highlight_null(null_color='red')
