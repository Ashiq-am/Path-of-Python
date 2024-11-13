def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans==ans[current_question-1]:
		user_score.set(user_score.get()+1)
