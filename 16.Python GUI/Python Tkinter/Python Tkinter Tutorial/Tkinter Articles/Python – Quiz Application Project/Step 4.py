if __name__ == "__main__":
	root = Tk()
	# setup basic window
	root.title("GFG QUIZ APP")
	root.geometry("850x520")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quiz App",
		font="calibre 40 bold",
		relief=SUNKEN, background="cyan",
		padx=10, pady=9).pack()
	Label(root, text="",
		font="calibre 10 bold").pack()
	start_button = Button(root, text="Start Quiz",
						command=start_quiz,
						font="calibre 17 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question",
						command=next_question,
						font="calibre 17 bold")

	root.mainloop()
