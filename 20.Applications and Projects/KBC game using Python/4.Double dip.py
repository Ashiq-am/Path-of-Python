def doubleDip(ran):

	# double dip gives 2 chances
	print("Select two options\n")
	trial1 = int(input())

	if answer[ran] == trial1:
		great = 1
		print("Correct Answer,well done....")
	else:
		print("Your first trial is wrong, choose another\t")
		trial2 = int(input())

		if answer[ran] == trial2:
			great = 1
			print("Correct Answer\t")
		else:
			print("Your second trial is also wrong..Better luck next time..\t")
			print("Correct Answer is :", options[answer[ran]-1][ran])
			great = 0

	return great
