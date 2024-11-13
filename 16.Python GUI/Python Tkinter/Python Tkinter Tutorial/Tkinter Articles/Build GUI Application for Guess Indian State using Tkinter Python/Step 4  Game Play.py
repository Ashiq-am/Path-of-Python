# we will run the game until our correct
# guesses include all the states
while len(correct_guesses) < 29:

    # create an input prompt to ask user
    # to enter a state name if he wants to
    # exit, he should enter "Exit"
    answer = screen.textinput(
        title=f'Guess the State {len(correct_guesses)}/29',
        prompt='Enter Name or "Exit" to Quit')

    # convert the user to Title case, which
    # is the case in which we have stored
    # our state names. We need to convert user
    # input in case he/she enter the name in
    # some other case
    answer = answer.title()

    # first check if the user want to quit.
    if answer == "Exit":
        # create a list of state names he missed
        # and store them in a dictionary
        missing_states = [n for n in states if n not in correct_guesses]
        missing_guess = {
            'State': missing_states
        }

        # create a datafram using Pandas method
        # and convert and store it as CSV file
        pandas.DataFrame(missing_guess).to_csv(
            'states_to_learn.csv', index=False)
        # break the game loop
        break

    # check if the anser user entered is in the
    # states list or not
    if answer in states:
        # extract that state's data from our data set
        state = data[data.State == answer]
        x_ = int(state.x)
        y_ = int(state.y)

        # add this correct answer to our correct
        # guesses list
        correct_guesses.append(answer)

        # now go to required coordinates and write
        # the state name
        pen.goto(x=x_, y=y_)
        pen.write(f"{answer}", font=('Arial', 8, 'normal'))
