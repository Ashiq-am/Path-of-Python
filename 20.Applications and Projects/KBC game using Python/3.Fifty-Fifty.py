def fifty(ran, op):
	print("Q."+questions[ran])

	for num, option in enumerate(op):
		print(str(num+1)+"."+option[ran])

	choice_fifty = int(input("enter your choice \t"))

	if choice_fifty == answer[ran]:
		print("Correct Answer.....")
		great = 1
	else:
		great = 0
		print("wrong answer")
		print("Correct Answer is :", options[answer[ran]-1][ran])

	return great
