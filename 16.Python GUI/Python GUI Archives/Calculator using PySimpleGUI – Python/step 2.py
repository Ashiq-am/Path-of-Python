# Result Value
Result = ''

# Make Infinite Loop
while True:
    # Button Values
    button, value = form.Read()

    # Check Press Button Values
    if button == 'c':
        Result = ''
        form.FindElement('input').Update(Result)
    elif button == '«':
        Result = Result[:-1]
        form.FindElement('input').Update(Result)
    elif len(Result) == 16:
        pass

    # Results
    elif button == '=':
        Answer = eval(Result)
        Answer = str(round(float(Answer), 3))
        form.FindElement('input').Update(Answer)
        Result = Answer
    # close the window
    elif button == 'Quit' or button == None:
        break
    else:
        Result += button
        form.FindElement('input').Update(Result)
