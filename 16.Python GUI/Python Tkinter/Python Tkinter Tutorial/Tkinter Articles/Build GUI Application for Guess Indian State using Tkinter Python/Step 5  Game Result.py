screen.clear()
pen.goto(0, 0)
end_text = ""
score = len(correct_guesses)

if score == 29:
	end_text = 'You Guessed Them All Correctly'
elif score >= 20:
	end_text = f"Good Work: {score}/29"
elif score >= 15:
	end_text = f"Average Performance: {score}/29"
else:
	end_text = f"Poor Performance: {score}/29"

pen.write(f"{end_text}", align='center', font=("Arial", 22, 'normal'))

turtle.mainloop()
