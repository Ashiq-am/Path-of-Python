# Prescribing the level(s) to be stacked
df_multi_level_cols2.stack(0)

# The first parameter controls which level
# or levels are stacked
df_multi_level_cols2.stack([0, 1])
