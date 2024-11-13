# Sum of digits of a number using divmod
num = 86
sums = 0
while num!=0:
	use = divmod(num, 10)
	dig = use[1]
	sums = sums + dig
	num = use[0]
print(sums)
