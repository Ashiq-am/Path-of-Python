data_with_ties = {
    'A': [5, 9, 9, 1, 7],
    'B': [10, 10, 6, 10, 4],
    'C': [7, 9, 2, 9, 5]
}

df_with_ties = pd.DataFrame(data_with_ties)
second_highest_with_ties = df_with_ties.apply(lambda x: x.nlargest(2).iloc[-1])
print("Second highest values with ties:\n", second_highest_with_ties)
