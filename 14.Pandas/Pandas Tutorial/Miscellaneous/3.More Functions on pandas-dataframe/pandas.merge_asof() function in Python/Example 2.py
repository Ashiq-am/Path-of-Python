# importing package
import pandas

# creating data
left = pandas.DataFrame({'a': [1, 5, 10],
						'left_val': ['a', 'b', 'c']})

right = pandas.DataFrame({'a': [1, 2, 3, 6, 7],
						'right_val': [1, 2, 3, 6, 7]})

# view data
print(left)
print(right)

# applying merge_asof on data
print(pandas.merge_asof(left, right, on='a',
						direction='forward'))
print(pandas.merge_asof(left, right, on='a',
						direction='nearest'))
