frequency = df.groupby(['date']).size().reset_index(name='frequency')
print(frequency)
