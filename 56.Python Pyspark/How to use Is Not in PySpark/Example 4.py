new_df = df.filter(df["age"].isNotNull() & df["marks"].isNotNull())
# or
# new_df = df.filter(df.age.isNotNull() & df.marks.isNotNull())
new_df.show()
