# extract the sample dataframe from "df"
# and store it in "sample_df"
from pandas.tests.groupby.test_value_counts import df

sample_df = df.sample(15)

# Print the sample data frame
sample_df
