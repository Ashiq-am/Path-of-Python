import sys

print('Regular integer: (maxint=%s)' % sys.maxint)
try:
	i = sys.maxint * 3
	print('No overflow for ', type(i), 'i =', i)
except OverflowError, err:
	print('Overflowed at ', i, err)


print('Long integer:')
for i in range(0, 100, 10):
	print('%2d' % i, 2L ** i)


print('Floating point values:')
try:
	f = 2.0**i
	for i in range(100):
		print(i, f)
		f = f ** 2
except OverflowError, err:
	print('Overflowed after', f, err)
