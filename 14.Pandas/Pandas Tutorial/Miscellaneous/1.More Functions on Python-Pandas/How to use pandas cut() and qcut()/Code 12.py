cut_series, cut_intervals = pd.cut(df.Year,
								bins=3,
								retbins=True)

print("Cut series:")
print(cut_series.head())
print()
print("Cut intervals: ", cut_intervals)
