data_with_nan = {
    'A': [5, 9, None, 1, 7],
    'B': [3, None, 6, 10, 4],
    'C': [None, 3, 2, 9, 5]
}

df_with_nan = pd.DataFrame(data_with_nan)
second_highest_with_nan = df_with_nan.apply(lambda x: x.nlargest(2).iloc[-1])
print("Second highest values with NaN:\n", second_highest_with_nan)
