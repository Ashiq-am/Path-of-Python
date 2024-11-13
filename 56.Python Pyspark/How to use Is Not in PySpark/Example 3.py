new_df = df.filter(df["marks"].isNotNull())
# or
# new_df = df.filter(df.marks.isNotNull())
new_df.show()
