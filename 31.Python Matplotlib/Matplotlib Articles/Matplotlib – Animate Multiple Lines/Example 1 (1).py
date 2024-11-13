# add random points for each line
l1 = [random.randint(-20, 4)+(points**1.88)/(random.randint(13, 14))
	for points in range(0, 160, 2)]
l2 = [random.randint(0, 9)+(points**1.9)/(random.randint(9, 11))
	for points in range(0, 160, 2)]
l3 = [random.randint(-10, 10)-(points**1.4)/(random.randint(9, 12))
	for points in range(0, 160, 2)]
l4 = [random.randint(-5, 10)-(points**1.1)/(random.randint(7, 12))
	for points in range(0, 160, 2)]
