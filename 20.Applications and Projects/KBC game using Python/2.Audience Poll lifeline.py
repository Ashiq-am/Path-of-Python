def audience(ran, opts):

	# graphical audience poll using pandas
	print("According to audience\n")

	s = pd.Series([opt1[ran], opt2[ran], opt3[ran], opt4[ran]],
				index=['1', '2', '3', '4'])

	s.plot.bar(figsize=(20, 10))
	plt.xlabel('Options')
	plt.ylabel('%')
	plt.title("Audience Poll")
	plt.show()

	print('1.', opts[0][ran], "%", '\t', '2.', opts[1][ran],
		"%", '\t', '3.',opts[2][ran], "%", '\t', '4.',
		opts[3][ran], "%", '\nenter your choice\t')

	print("Would you like to take lifeline again,if yes then\
	press 9 or Press 0 to Quit\t")

	choice = int(input())

	if choice == 9:
		great = lifeline(ran, opts, op)
		return great
	elif choice == answer[ran]:
		great = 1
		print("Correct answer,well done!..")
	elif choice == 0:
		great = -2
	else:
		great = 0
		print("Incorrect")
		print("Correct Answer is :", options[answer[ran]-1][ran])

	return great
