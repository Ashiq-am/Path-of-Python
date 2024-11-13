def result():
	global count
	number=userv.get()
	if number=='':
		tmsg.showerror('Error',"Please enter a value")
	else:
		n=int(number)
		count+=1
		if count==10:
			a=tmsg.showinfo('Game over','You loose the Game!')
		elif comp==n:
			score=11-count
			a=tmsg.showinfo('Win',f'You guess right number!\nYour score {score}')
			show.config(text='Winn!',fg='green')
			with open('score.txt','w') as f:
				f.write(str(score))
			generate()
			tmsg.showinfo('Next number',f'click ok to Guess another number')
		elif comp>n:
			show.config(text='Select greater number',fg='red')
		else:
			show.config(text='Select smaller number',fg='red')
