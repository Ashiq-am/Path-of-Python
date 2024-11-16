series_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series_b = pd.Series([4, 5], index=['b', 'c'])
sum_series = series_a + series_b
print(sum_series)
