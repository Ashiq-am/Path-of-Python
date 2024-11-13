# Split DataFrame into even and odd ranks
df_even_rank = df_rank.filter(df_rank.rank % 2 == 0)
df_odd_rank = df_rank.filter(df_rank.rank % 2 != 0)

# Show even rank DataFrame
df_even_rank.show()

# Show odd rank DataFrame
df_odd_rank.show()
