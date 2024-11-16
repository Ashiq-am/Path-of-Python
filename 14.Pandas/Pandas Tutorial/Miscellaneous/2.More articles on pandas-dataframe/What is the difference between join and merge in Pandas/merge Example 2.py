merged_df = left.merge(right, left_index=True,
					right_index=True, suffixes=['_', ''])
print(merged_df)
