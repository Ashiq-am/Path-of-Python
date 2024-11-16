frequency = df.groupby(['date', 'value']).size().reset_index(name='frequency')
print(frequency)
