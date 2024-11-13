import work
print ("GCD : ", work.gcd(12,8))

print ("\nDivision : ", work.divide(42,8))

pt1 = work.Point(2,3)
pt2 = work.Point(4,5)

print ("\nDistance between pt1 and pt2 : ",
	work.distance(pt1,pt2))


print ("\nx co-ordinate of pt1 : ", pt1.x)
print ("\ny co-ordinate of pt1 : ", pt1.x)


import array
ar = array.array('d',[2, 4, 6])
print ("\nAverage : ", work.avg(arr))
