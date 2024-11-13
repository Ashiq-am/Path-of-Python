from scipy.integrate import quad

def f(x):
    return 3.0*x*x + 1.0

I, err = quad(f, 0, 1)
print(I)
print(err)
