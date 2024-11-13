# Since the above data is in wide
# form we convert it into long
# form using melt function
data_df = df.melt(var_name='Pulses',
				value_name='Tons Consumed')
print(data_df)
