# function to calculate the
# price of all the orders


def calculate():
    # dic for storing the food quantity and price
    dic = {'aloo_partha': [e1, 30],
           'samosa': [e2, 5],
           'pizza': [e3, 150],
           'chilli_potato': [e4, 50],
           'chowmein': [e5, 70],
           'gulab_jamun': [e6, 35]}
    total = 0

    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get()) * val[1]
    label16 = Label(window,
                    text="Your Total Bill is - " + str(total),
                    font="times 18")

    # position
    label16.place(x=20, y=490)

    # it will update the label with a new one
    label16.after(1000, label16.destroy)

    # refreshing the window
    window.after(1000, calculate)


# execute calculate function after 1 second
window.after(1000, calculate)
window.mainloop()
