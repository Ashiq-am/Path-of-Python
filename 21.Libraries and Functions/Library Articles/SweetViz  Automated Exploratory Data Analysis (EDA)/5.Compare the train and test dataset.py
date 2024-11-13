# Split the dataset
train_df, test_df = train_test_split(df, train_size=0.75)
# compare the dataset
compare = sv.compare(source=train_df, compare=test_df, target_feat="MedHouseVal")

# Show the result
compare.show_html('Compare.html')
