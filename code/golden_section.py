from function import *


def golden_section(f, a, b, eps, min_max):
    phi = (np.sqrt(5) + 1) / 2

    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    while abs(b - a) > eps:
        if min_max == 'min':
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1
        else:
            if f(x1) >= f(x2):
                b = x2
            else:
                a = x1

        # We recompute c and d  to avoid loss of precision
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

    # extremum is between current bounds
    ans = (b + a) / 2
    return round(ans, 2), round(f(ans), 2)
