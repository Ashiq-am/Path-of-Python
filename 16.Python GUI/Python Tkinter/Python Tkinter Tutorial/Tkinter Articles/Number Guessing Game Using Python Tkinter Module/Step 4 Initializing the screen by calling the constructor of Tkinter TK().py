app = Tk()
basic()
count = 0
comp = random.randint(1, 101) # generating random values between 1 to 100
userv = StringVar() # variable to getting input in string format

# creating input field
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT,
			borderwidth=2, font='Helvicta 18 bold').pack(pady=10)

# submit button
i = Image.open('bt.jpg')
resized_image = i.resize((150, 50), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
submit = Button(app, image=new_image, command=result,
				font='Helvicta 18 bold', relief=FLAT).pack(pady=10)
show = Label(app, text='', font='Helvicta 12 bold')
show.pack(pady=10)
