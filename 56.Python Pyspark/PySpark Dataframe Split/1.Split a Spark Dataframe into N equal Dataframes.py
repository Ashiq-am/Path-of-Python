import pyspark
import pandas as pd

session = pyspark.sql.SparkSession.builder.getOrCreate()


def split_df_into_N_equal_dfs(d, df, n):
    if df.count() / n == int(df.count() / n):
        rows = df.count() / n
        start = 0
        d_ix = 0
        for i in range(1, df.count() + 1):
            if i % rows == 0:
                d[d_ix] = session.createDataFrame(
                    df.collect()[start:i])
                d_ix += 1
                start = i
    else:
        print('Cannot make given number of\
	equal DataFrames from the DataFrame')


# making DataFrame in Pandas and
# converting ot to a PySpark DataFrame.
df = pd.DataFrame({
    'Odd_Numbers': [y for y in range(1,
                                     17, 2)],
    'Even_Numbers': [x for x in range(2,
                                      17, 2)],
})

sp_df = session.createDataFrame(df)

print("Original Data frame")
sp_df.show()
# creating an empty dictionary
# to store splitted DataFrames.
df_dict = {}

# using the function to split the
# DataFrame into two equal DataFrames
split_df_into_N_equal_dfs(df_dict,
                          sp_df, 2)

print("Splitted Data frame")
df_dict[0].show()
df_dict[1].show()
