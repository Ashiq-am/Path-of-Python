new_df = df.filter(df["age"].isNotNull())
# or
# new_df = df.filter(df.age.isNotNull())
new_df.show()
