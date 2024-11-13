# store all the numbers in a variable
numberpad = "789456123"

# here i will count the rows for placing buttons
# in grid
i = 0

# create an empty list to store
# each button with its particular specifications
btn = []

# j is in that range to place
# the button in that particular row
for j in range(2, 5):

		# k is in this range to place the
	# button in that particular column
	for k in range(3):
		btn.append(Button(calc,
						width=6,
						height=2,
						bg='black',
						fg='white',
						font=('Helvetica', 20, 'bold'),
						bd=4, text=numberpad[i]))

		# set buttons in row & column and
		# separate them with a padding of 1 unit
		btn[i].grid(row=j, column=k, pady=1)

		# put that number as a symbol on that button
		btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
		i += 1
