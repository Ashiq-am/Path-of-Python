""

'''Print the number of athletes who are gold medalists and whose 
age is greater than 50 with their info'''




goldMedals = merged[(merged.Medal == 'Gold')]
print('The no of athletes is',
	goldMedals['ID'][goldMedals['Age'] > 50].count(), '\n')
print(goldMedals[goldMedals['Age'] > 50])
