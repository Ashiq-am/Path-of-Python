def basic():
	# setup the window size, title, logo
	app.title("Number Guessing game")
	app.geometry("500x500")
	app.minsize(500, 500)
	app.maxsize(500, 500)
	photo = PhotoImage(file="guess.png")
	app.iconphoto(False, photo)
	heading = Label(text='Number Guessing game', font="Helvicta 18 bold",
					bg='black', fg='tomato', padx=170).pack()
	with open('score.txt', 'r') as f:
		hg = f.read()
	sc = Label(app, text=f'Previous score: {hg}', font='lucida 8 bold ').pack(
		anchor=E, padx=25, pady=5)

	# footer
	footer = Label(text='Developed by Siddharth Dyamgond', font="Helvicta 8 bold",
				bg='black', fg='tomato', padx=153).pack(side=BOTTOM)

	# Setup Menu
	mymenu = Menu(app)
	filee = Menu(mymenu, tearoff=0)
	mymenu.add_cascade(label='Start', menu=filee)
	mymenu.add_cascade(label='Restart', command=restart)
	mymenu.add_command(label='About', command=call1)
	mymenu.add_command(label='Quit', command=quit)
	app.config(menu=mymenu)
	generate()
