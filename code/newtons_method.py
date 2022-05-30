from function import *

def newton(f0, x0, eps, max_iter):

    f = diff_(f0)
    F = diff_(f)

    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < eps:
            # print('Found solution after',n,'iterations.')
            return xn
        Fxn = F(xn)
        if Fxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Fxn
    print('Exceeded maximum iterations. No solution found.')
    return None
