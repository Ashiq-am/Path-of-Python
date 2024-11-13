def solve(equation):
    # replacing all the x terms with j
    # the imaginary part
    s1 = equation.replace('x', 'j')

    # shifting the equal sign to start
    # an opening bracket
    s2 = s1.replace('=', '-(')

    # adding the closing bracket to form
    # a complete expression
    s = s2 + ')'

    # mapping the literal j to the complex j
    z = eval(s, {'j': 1j})
    real, imag = z.real, -z.imag

    # if the imaginary part is true return the
    # answer
    if imag:
        return "x = %f" % (real / imag)
    else:
        if real:
            return "No solution"
        else:
            return "Infinite solutions"


equation = "x=x+10"
print(solve(equation))
