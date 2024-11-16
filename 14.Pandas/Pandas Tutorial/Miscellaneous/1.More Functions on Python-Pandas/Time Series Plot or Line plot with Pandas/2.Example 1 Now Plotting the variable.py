# use plot() method on the dataframe
df_days_calories.plot( 'day' , 'calories' )

# Alternatively, you can use .set_index
# to set the data of each axis as follows:
# df_days_calories.set_index('day')['calories'].plot();
