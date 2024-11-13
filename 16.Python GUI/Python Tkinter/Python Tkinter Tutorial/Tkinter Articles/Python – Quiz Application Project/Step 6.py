def next_question():
	global current_question
	if current_question<len(question):
		# get key or question that need to be printed
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		# clear frame to update its content
		clear_frame()
		# printing question
		Label(f1,text=f"Question : {c_question}",padx=15,font="calibre 12 normal").pack(anchor=NW)
		# printing options
		for option in question[c_question]:
			Radiobutton(f1,text=option,variable=user_ans,value=option,padx=28).pack(anchor=NW)
		current_question+=1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1,text=output,font="calibre 25 bold").pack()
		Label(f1,text="Thanks for Partcipating",font="calibre 18 bold").pack()
